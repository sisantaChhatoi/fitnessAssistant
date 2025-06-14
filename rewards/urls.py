from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BadgeViewSet, AchievementViewSet

router = DefaultRouter()
router.register(r'badges', BadgeViewSet)
router.register(r'achievements', AchievementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
