from rest_framework import serializers
from .models import Doctor, Direction

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ("name", "slag", "directions","description" ,"date" ,"years_of_experience" ,"number_sort")

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["directions"] = DirectionSerializer(instance.directions.all(), many=True).data
        return rep

class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = ("name", "slag", "number_sort")
