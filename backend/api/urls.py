from django.urls import path

from . import views

urlpatterns = [
    path("health/", views.health),
    path("members/", views.members),
    path("sightings/", views.sightings),
    path("animal_sightings/", views.animal_sightings),
    path("vegetation_sightings/", views.vegetation_sightings),
    path("image/", views.image),
]