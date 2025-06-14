from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from datetime import datetime, timedelta
import random

from .models import Plan, GeneratedPerDayPlan
from .serializers import PlanSerializer, GeneratedPerDayPlanSerializer
from exercises.models import Exercise

# Create your views here.
class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        plan = serializer.save()

        # Create a new GeneratedPerDayPlan with default values
        self._create_daily_plan(plan)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def _create_daily_plan(self, plan):
        # Create a new GeneratedPerDayPlan with day_no set to parent's completion_count + 1
        day_no = plan.completion_count + 1
        daily_plan = GeneratedPerDayPlan.objects.create(
            plan=plan,
            day_no=day_no,
        )

        # Get random exercises (6-8)
        exercises = self._get_random_exercises(plan.objectiveType)
        daily_plan.exercises.set(exercises)

        return daily_plan

    def _get_random_exercises(self, objective_type):
        # Get exercises matching the objective type
        matching_exercises = Exercise.objects.filter(objectiveType=objective_type)

        # If not enough matching exercises, get any exercises
        if matching_exercises.count() < 6:
            matching_exercises = Exercise.objects.all()

        # Get random 6-8 exercises
        count = random.randint(6, 8)
        if matching_exercises.count() <= count:
            return matching_exercises

        return random.sample(list(matching_exercises), count)

class GeneratedPerDayPlanViewSet(viewsets.ModelViewSet):
    queryset = GeneratedPerDayPlan.objects.all()
    serializer_class = GeneratedPerDayPlanSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # Check if completion_status is being updated to True
        if 'completion_status' in request.data and request.data['completion_status'] and not instance.completion_status:
            # Set completed_at to current time
            instance.completed_at = datetime.now()

            # Update parent plan's completion_count
            plan = instance.plan
            plan.completion_count += 1

            # Check if completed_at and created_at differ by more than one day
            if instance.completed_at and instance.created_at:
                time_diff = instance.completed_at - instance.created_at
                if time_diff.days > 1:
                    # Set parent plan's streak_count to 0
                    plan.streak_count = 0
                else:
                    # Increase parent plan's streak_count by 1
                    plan.streak_count += 1

            plan.save()

            # Create a new daily plan
            PlanViewSet()._create_daily_plan(plan)

        self.perform_update(serializer)
        return Response(serializer.data)
