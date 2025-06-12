from django.db import models

from customers.models import Customer
from exercises.models import Exercise
from objectiveArray import speciality


# Create your models here.
class Plan(models.Model):
    objectiveType = models.CharField(max_length=5,choices=speciality)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='plans')
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True)
    duration_in_days = models.IntegerField(default=7)
    completion_count = models.IntegerField(default=0)
    streak_count = models.IntegerField()
    completion_status = models.BooleanField(default=False)

class GeneratedPerDayPlan(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE,related_name='GeneratedPerDayPlans')
    day_no = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True)
    exercises = models.ManyToManyField(Exercise)
    completion_status = models.BooleanField(default=False)