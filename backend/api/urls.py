from django.urls import path

from . import auth_views, views

urlpatterns = [
    path("health/", views.health),
    path("auth/register/", auth_views.register),
    path("auth/login/", auth_views.login),
    path("auth/logout/", auth_views.logout),
    path("auth/me/", auth_views.me),
    path("members/", views.members),
    path("sightings/", views.sightings),
    path("animal_sightings/", views.animal_sightings),
    path("vegetation_sightings/", views.vegetation_sightings),
    path("image/", views.image),
    path("species/", views.species),
    path("regions/", views.regions),
    path("habitats/", views.habitats),
    path("weather/", views.weather_conditions),
    path("hunting_seasons/", views.hunting_seasons),
]