from rest_framework import serializers
from .models import Badge, Achievement

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ['id', 'name', 'description', 'badgeImage', 'points_needed']

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ['id', 'name', 'description', 'achievementImage']
