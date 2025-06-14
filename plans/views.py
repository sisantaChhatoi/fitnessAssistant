from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from datetime import datetime, timedelta
from django.utils import timezone
import random
from django_filters import rest_framework as filters

from .models import Plan, GeneratedPerDayPlan
from .serializers import PlanSerializer, GeneratedPerDayPlanSerializer
from .filters import PlanFilter, GeneratedPerDayPlanFilter
from exercises.models import Exercise

# Create your views here.

def select_exercises_for_daily_plan(plan, day_no):
    """
    Helper method to select exercises for a daily plan based on:
    1. Parent plan's objective type (WL, BB, FG)
    2. Day number (increasing difficulty as day_no increases)
    3. Exercise difficulty levels (E, M, H)

    Returns a queryset of 5-8 exercises.
    """
    objective_type = plan.objectiveType

    # Calculate difficulty distribution based on day_no
    # As day_no increases, we increase the proportion of hard and medium exercises
    # For simplicity, we'll use a linear progression
    hard_ratio = min(0.1 + (day_no * 0.05), 0.6)  # Start at 10%, increase by 5% per day, max 60%
    medium_ratio = min(0.3 + (day_no * 0.03), 0.5)  # Start at 30%, increase by 3% per day, max 50%
    easy_ratio = max(1 - hard_ratio - medium_ratio, 0)  # The rest are easy exercises

    # Determine how many exercises to select (between 5 and 8)
    total_exercises = random.randint(5, 8)

    # Calculate how many of each difficulty to select
    hard_count = round(total_exercises * hard_ratio)
    medium_count = round(total_exercises * medium_ratio)
    easy_count = total_exercises - hard_count - medium_count

    # Adjust if we ended up with too few or too many due to rounding
    while hard_count + medium_count + easy_count != total_exercises:
        if hard_count + medium_count + easy_count < total_exercises:
            easy_count += 1
        else:
            if easy_count > 0:
                easy_count -= 1
            elif medium_count > 0:
                medium_count -= 1
            else:
                hard_count -= 1

    # Get exercises matching the plan's objective type (with higher priority)
    matching_exercises = Exercise.objects.filter(objectiveType=objective_type)

    # Get all exercises for fallback
    all_exercises = Exercise.objects.all()

    selected_exercises = []

    # Select hard exercises
    hard_matching = list(matching_exercises.filter(toughnessLevel='H'))
    hard_all = list(all_exercises.filter(toughnessLevel='H'))

    # Prioritize matching exercises, fall back to any if needed
    if len(hard_matching) >= hard_count:
        selected_exercises.extend(random.sample(hard_matching, hard_count))
    else:
        selected_exercises.extend(hard_matching)  # Add all matching hard exercises
        remaining = hard_count - len(hard_matching)
        # Exclude already selected exercises
        remaining_hard = [ex for ex in hard_all if ex not in selected_exercises]
        if remaining > 0 and remaining_hard:
            selected_exercises.extend(random.sample(remaining_hard, min(remaining, len(remaining_hard))))

    # Select medium exercises
    medium_matching = list(matching_exercises.filter(toughnessLevel='M'))
    medium_all = list(all_exercises.filter(toughnessLevel='M'))

    # Prioritize matching exercises, fall back to any if needed
    if len(medium_matching) >= medium_count:
        selected_exercises.extend(random.sample(medium_matching, medium_count))
    else:
        selected_exercises.extend(medium_matching)  # Add all matching medium exercises
        remaining = medium_count - len(medium_matching)
        # Exclude already selected exercises
        remaining_medium = [ex for ex in medium_all if ex not in selected_exercises]
        if remaining > 0 and remaining_medium:
            selected_exercises.extend(random.sample(remaining_medium, min(remaining, len(remaining_medium))))

    # Select easy exercises
    easy_matching = list(matching_exercises.filter(toughnessLevel='E'))
    easy_all = list(all_exercises.filter(toughnessLevel='E'))

    # Prioritize matching exercises, fall back to any if needed
    if len(easy_matching) >= easy_count:
        selected_exercises.extend(random.sample(easy_matching, easy_count))
    else:
        selected_exercises.extend(easy_matching)  # Add all matching easy exercises
        remaining = easy_count - len(easy_matching)
        # Exclude already selected exercises
        remaining_easy = [ex for ex in easy_all if ex not in selected_exercises]
        if remaining > 0 and remaining_easy:
            selected_exercises.extend(random.sample(remaining_easy, min(remaining, len(remaining_easy))))

    # If we still don't have enough exercises, add random ones
    if len(selected_exercises) < total_exercises:
        remaining = total_exercises - len(selected_exercises)
        remaining_exercises = [ex for ex in all_exercises if ex not in selected_exercises]
        if remaining_exercises:
            selected_exercises.extend(random.sample(remaining_exercises, min(remaining, len(remaining_exercises))))

    return selected_exercises

class PlanViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Plans that allows GET, POST, and PATCH operations.
    """
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    http_method_names = ['get', 'post', 'patch', 'head']
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PlanFilter

    def create(self, request, *args, **kwargs):
        """
        Create a new Plan and automatically create the first GeneratedPerDayPlan.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        plan = serializer.save()

        # Create the first daily plan
        daily_plan = GeneratedPerDayPlan.objects.create(
            plan=plan,
            day_no=1
        )

        # If exercises were provided in the request, use those
        if 'exercises' in request.data:
            daily_plan.exercises.set(request.data['exercises'])
        else:
            # Otherwise, select exercises based on our logic
            selected_exercises = select_exercises_for_daily_plan(plan, 1)
            daily_plan.exercises.set(selected_exercises)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class GeneratedPerDayPlanViewSet(viewsets.ModelViewSet):
    """
    API endpoint for GeneratedPerDayPlans that allows GET, POST, and PATCH operations.
    """
    queryset = GeneratedPerDayPlan.objects.all()
    serializer_class = GeneratedPerDayPlanSerializer
    http_method_names = ['get', 'post', 'patch', 'head']
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GeneratedPerDayPlanFilter

    def partial_update(self, request, *args, **kwargs):
        """
        Handle PATCH requests with special logic for completion_status.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # Check if completion_status is being updated to True
        if 'completion_status' in request.data and request.data['completion_status'] == True and not instance.completion_status:
            # Set completed_at field
            instance.completed_at = timezone.now()

            # Increase completion_count of parent plan by 1
            parent_plan = instance.plan
            parent_plan.completion_count += 1

            # Increment customer's points by 10
            customer = parent_plan.customer
            customer.points += 10
            customer.save()

            # Check if completion_count equals duration_in_days, if yes set completed_at
            if parent_plan.completion_count == parent_plan.duration_in_days:
                parent_plan.completed_at = timezone.now()

                # Increment customer's points by 20 when plan is completed
                customer.points += 20
                customer.save()

            # Update streak_count based on created_at and completed_at difference
            if instance.created_at and instance.completed_at:
                time_diff = instance.completed_at - instance.created_at
                if time_diff.days < 1:  # Less than 24 hours
                    parent_plan.streak_count += 1  # Increment by 1
                else:
                    parent_plan.streak_count = 0  # Set to 0 if more than 24 hours

            # Save the parent plan
            parent_plan.save()

            # Only create a new daily plan if this is not the last day
            new_day_no = parent_plan.completion_count + 1
            if new_day_no <= parent_plan.duration_in_days:
                new_daily_plan = GeneratedPerDayPlan.objects.create(
                    plan=parent_plan,
                    day_no=new_day_no
                )

                # Select exercises based on our logic
                selected_exercises = select_exercises_for_daily_plan(parent_plan, new_day_no)
                new_daily_plan.exercises.set(selected_exercises)

        # Save the updated instance
        serializer.save()

        return Response(serializer.data)
