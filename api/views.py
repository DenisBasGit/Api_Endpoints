import django_filters.rest_framework
from django.shortcuts import render
from rest_framework import generics, filters
from .models import *
from .serializers import DoctorSerializer, DirectionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .service import DoctorFilter
from rest_framework.filters import SearchFilter, OrderingFilter

class ApiView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = DoctorFilter
    search_fields = ('name', 'years_of_experience', 'direction__name')

class SortView(generics.ListAPIView):
    queryset = Doctor.objects.order_by('number_sort', 'name')
    serializer_class = DoctorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['number_sort', 'name','years_of_experience']


class DirectionView(generics.ListAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer
