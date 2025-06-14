from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlanViewSet, GeneratedPerDayPlanViewSet

router = DefaultRouter()
router.register(r'plans', PlanViewSet)
router.register(r'daily-plans', GeneratedPerDayPlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]