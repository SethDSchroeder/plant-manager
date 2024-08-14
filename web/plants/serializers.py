from rest_framework import serializers
from .models import Plant, Greenhouse

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('id', 'name', 'scientific_name', 'location', 'soil_moisture')