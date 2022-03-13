from django.contrib import auth
from django.urls import path

# Register your models here.
from django.apps import AppConfig

class DepartamentoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "departamento"

def DesdeApps(self):
    print("-------- desde la app departamento --------")
    
urlpatterns = [
    path("departamento/", DesdeApps)
]
    