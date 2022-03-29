from unicodedata import name
from django.apps import AppConfig
from django.urls import path

class CuentaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = 'cuenta'

def MostrarUbicacion(self):
    print ("********** MODULO CUENTA *********")

urlpatterns = [
    path("cuenta/", MostrarUbicacion)
]