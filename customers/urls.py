from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, AuthView

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('authenticate/', AuthView.as_view(), name='authenticate'),
]
