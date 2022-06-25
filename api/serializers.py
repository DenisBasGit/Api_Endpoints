from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ("name", "slag", "direction","description" ,"date" ,"years_of_experience" ,"number_sort")