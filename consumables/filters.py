from django_filters import rest_framework as filters
from .models import FoodItem, Recipe

class FoodItemFilter(filters.FilterSet):
    objective_type = filters.CharFilter(field_name='objectiveType')
    kind = filters.CharFilter(field_name='kind')

    class Meta:
        model = FoodItem
        fields = ['objectiveType', 'kind']

class RecipeFilter(filters.FilterSet):
    objective_type = filters.CharFilter(field_name='objectiveType')
    kind = filters.CharFilter(field_name='kind')

    class Meta:
        model = Recipe
        fields = ['objectiveType', 'kind']