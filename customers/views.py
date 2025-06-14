from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters import rest_framework as filters
from .models import Customer
from .serializers import CustomerSerializer, AuthSerializer, UserSerializer
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

class AuthView(APIView):
    """
    API endpoint for user authentication.
    Accepts username, email, and password and returns the user object if authentication is successful.
    """
    def post(self, request):
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
