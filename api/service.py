from django_filters import rest_framework as filters
from .models import *
from django.db import models

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class DoctorFilter(filters.FilterSet):
    name = CharFilterInFilter(field_name='doctor__name', lookup_expr='in')
    experience = filters.RangeFilter()

    class Meta:
        model = Doctor
        fields = ['name', 'experience']