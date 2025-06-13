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

    def __str__(self):
        return self.name


class Job(models.Model):
    customer = models.ForeignKey(Exercise, on_delete=models.CASCADE,related_name='jobs_of_customer')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE,related_name='jobs')
    completed_at = models.DateTimeField(null=True, blank=True)