from django_filters import rest_framework as filters
from .models import Customer

class CustomerFilter(filters.FilterSet):
    gender = filters.CharFilter(field_name='gender')
    kind = filters.CharFilter(field_name='kind')
    
    class Meta:
        model = Customer
        fields = ['gender', 'kind']