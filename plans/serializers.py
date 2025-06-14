from rest_framework import serializers
from .models import Plan, GeneratedPerDayPlan
from exercises.models import Exercise

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'objectiveType', 'customer', 'created_at', 'completed_at', 
                  'duration_in_days', 'completion_count', 'streak_count']
        read_only_fields = ['created_at', 'completed_at', 'completion_count', 'streak_count']

class GeneratedPerDayPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneratedPerDayPlan
        fields = ['id', 'plan', 'day_no', 'created_at', 'completed_at', 
                  'exercises', 'completion_status']
        read_only_fields = ['created_at', 'completed_at']