from django_filters import rest_framework as filters
from .models import Customer

class CustomerFilter(filters.FilterSet):
    gender = filters.CharFilter(field_name='gender')
    kind = filters.CharFilter(field_name='kind')
    user__id = filters.NumberFilter(field_name='user__id')

    class Meta:
        model = Customer
        fields = ['gender', 'kind', 'user__id']
