from django.contrib import auth
from django.urls import path

from django.apps import AppConfig

class persona(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "persona"

def DesdeApps(self):
    print("-------- desde la app persona --------")
    
urlpatterns = [
    path("persona/", DesdeApps)
]
    