from django.db import models
from objectiveArray import speciality
# Create your models here.
foodKind = [
    ('VG','Vegetarian'),
    ('NVG','Non - Vegetarian')
]



class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    benefits = models.TextField(null=True, blank=True)
    calories = models.IntegerField()
    foodPicture = models.ImageField(upload_to='images/')
    objectiveType = models.CharField(max_length=5,choices=speciality)
    kind=models.CharField(max_length=5,choices=foodKind)

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    totalCalories = models.IntegerField()
    recipeImage = models.ImageField(upload_to='images/')
    kind=models.CharField(max_length=5,choices=foodKind)
    objectiveType = models.CharField(max_length=5,choices=speciality)

