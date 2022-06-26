from rest_framework import serializers
from .models import Doctor, Direction

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ("name", "slag", "direction","description" ,"date" ,"years_of_experience" ,"number_sort")

class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = ("name", "slag", "number_sort")