from rest_framework import serializers
from .models import Exercise, Job

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description', 'toughnessLevel', 'objectiveType', 'giphy']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'customer', 'exercise', 'completed_at']
