from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodItemViewSet, RecipeViewSet

router = DefaultRouter()
router.register(r'food-items', FoodItemViewSet)
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]