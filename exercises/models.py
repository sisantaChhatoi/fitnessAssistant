from django.db import models
from objectiveArray import speciality
# Create your models here.
toughness_level_array = [
    ('H','Hard'),
    ('M','Medium'),
    ('E','Easy')
]

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    toughnessLevel = models.CharField(max_length=4,choices=toughness_level_array)
    objectiveType = models.CharField(max_length=5,choices=speciality)
    giphy = models.ImageField(upload_to='giphys/')
