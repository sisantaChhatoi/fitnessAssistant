from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import FoodItem, Recipe
from .serializers import FoodItemSerializer, RecipeSerializer
from .filters import FoodItemFilter, RecipeFilter

# Create your views here.
class FoodItemViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows FoodItems to be viewed.
    """
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FoodItemFilter

class RecipeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Recipes to be viewed.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RecipeFilter
