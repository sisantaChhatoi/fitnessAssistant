from django_filters import rest_framework as filters
from .models import Plan, GeneratedPerDayPlan

class PlanFilter(filters.FilterSet):
    customer = filters.NumberFilter(field_name='customer')
    objective_type = filters.CharFilter(field_name='objectiveType')

    class Meta:
        model = Plan
        fields = ['customer', 'objectiveType']

class GeneratedPerDayPlanFilter(filters.FilterSet):
    plan = filters.NumberFilter(field_name='plan')
    completion_status = filters.BooleanFilter(field_name='completion_status')

    class Meta:
        model = GeneratedPerDayPlan
        fields = ['plan', 'completion_status']