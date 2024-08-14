from django.db import models

# Create your models here.

class Greenhouse (models.Model):
    name = models.CharField(max_length = 50, unique = False)
    temp = models.IntegerField()
    humidity = models.IntegerField()


class Plant (models.Model): 
    name = models.CharField(max_length = 50, unique = False)
    scientific_name = models.CharField(max_length = 50, unique = False)
    location = models.IntegerField() #This will be the greenhouse where the plant is located
    soil_moisture = models.IntegerField()

