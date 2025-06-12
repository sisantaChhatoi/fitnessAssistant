from django.db import models

# Create your models here.

class Achievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.name
    achievementImage = models.ImageField(upload_to='images/achievements/')

class Badge(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50,null=True,blank=True)
    badgeImage = models.ImageField(upload_to='images/badges/')
    points_needed = models.IntegerField(default=100)
    def __str__(self):
        return self.name

