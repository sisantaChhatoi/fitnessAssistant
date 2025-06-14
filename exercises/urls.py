from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExerciseViewSet, JobViewSet

router = DefaultRouter()
router.register(r'exercises', ExerciseViewSet)
router.register(r'jobs', JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
