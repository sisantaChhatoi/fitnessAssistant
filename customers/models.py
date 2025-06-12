from django.contrib.auth.models import User
from django.db import models

from rewards.models import Achievement, Badge

gender_type_array = [
    ('M', 'Male'),
    ('F', 'Female'),
]
# Create your models here.
class Customer(models.Model):
    age = models.IntegerField(null=True)
    height = models.DecimalField(max_digits=5,decimal_places=2,null=True)
    weight = models.DecimalField(max_digits=5,decimal_places=2,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=gender_type_array,max_length=2,default='M')
    points = models.IntegerField(default=0)
    achievements = models.ManyToManyField(Achievement,blank=True)
    kind = models.CharField(max_length=5,choices=[('VG','Vegetarian'),('NVG','Non-Vegetarian')],default='NVG')
    badges = models.ManyToManyField(Badge,blank=True,)

    def __str__(self):
        return self.user.username



