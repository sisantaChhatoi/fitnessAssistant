from rest_framework import serializers
from .models import FoodItem, Recipe

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ['id', 'name', 'benefits', 'calories', 'foodPicture', 'objectiveType', 'kind']

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'totalCalories', 'recipeImage', 'kind', 'objectiveType']