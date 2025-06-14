from django_filters import rest_framework as filters
from .models import Exercise

class ExerciseFilter(filters.FilterSet):
    toughness_level = filters.CharFilter(field_name='toughnessLevel')
    objective = filters.CharFilter(field_name='objectiveType')

    class Meta:
        model = Exercise
        fields = ['toughnessLevel', 'objectiveType']