from django.shortcuts import render
from rest_framework import viewsets
from .models import Badge, Achievement
from .serializers import BadgeSerializer, AchievementSerializer

# Create your views here.
class BadgeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Badges to be viewed and updated.
    """
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    http_method_names = ['get', 'post', 'patch', 'head']

class AchievementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Achievements to be viewed and updated.
    """
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    http_method_names = ['get', 'post', 'patch', 'head']
