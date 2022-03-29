from unicodedata import name
from django.apps import AppConfig
from django.urls import path

class LibroConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = 'libro'

def MostrarUbicacion(self):
    print ("********** MODULO LIBRO *********")

urlpatterns = [
    path("libro/", MostrarUbicacion)
]