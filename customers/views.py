from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import Customer
from .serializers import CustomerSerializer
from .filters import CustomerFilter

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Customers that allows GET, POST, and PATCH operations.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    http_method_names = ['get', 'post', 'patch', 'head']
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CustomerFilter
