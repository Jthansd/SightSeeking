from django.db import models
from django.conf import settings

# Create your models here.

class Sighting(models.Model):
    class sighting_type(models.TextChoices):
        ANIMAL = 'ANIMAL', 'Animal'
        VEGETATION = 'VEGETATION', 'Vegetation'
        VIEWING = 'VIEWING', 'Viewing'
        OTHER = 'OTHER', 'Other'
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sighting_type = models.CharField(max_length=20, choices=sighting_type.choices)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    locationLongitude = models.FloatField()
    locationLatitude = models.FloatField()

class Animal_Sighting(models.Model):
    sighting = models.OneToOneField(Sighting, on_delete=models.CASCADE, primary_key=True)
    common_name = models.CharField(max_length=100)
    species = models.CharField(max_length=100, blank=True, default='')

class Vegetation_Sighting(models.Model):
    sighting = models.OneToOneField(Sighting, on_delete=models.CASCADE, primary_key=True)
    common_name = models.CharField(max_length=100)
    species = models.CharField(max_length=100, blank=True, default='')

class Image_Sighting(models.Model):
    sighting = models.OneToOneField(Sighting, on_delete=models.CASCADE, primary_key=True)
    image_url = models.URLField(max_length=200)

    


