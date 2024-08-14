from django.shortcuts import render
from rest_framework import generics
from .models import Plant
from .serializers import PlantSerializer

# Create your views here.

class PlantView(generics.ListAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer