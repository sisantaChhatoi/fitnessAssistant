from django.shortcuts import render
from rest_framework import viewsets, filters as rest_filters
from django_filters import rest_framework as filters
from .models import Exercise, Job
from .serializers import ExerciseSerializer, JobSerializer
from .filters import ExerciseFilter

# Create your views here.
class ExerciseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Exercises to be viewed.
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ExerciseFilter

class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Jobs to be viewed, created, and deleted.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    http_method_names = ['get', 'post', 'delete', 'head']
    filter_backends = (rest_filters.OrderingFilter,)
    ordering_fields = ['completed_at']
    ordering = ['completed_at']
