from django.contrib import auth
from django.urls import path
# importo el paquete de vistas
from . import views
# Register your models here.
from django.apps import AppConfig

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "Home"
  
urlpatterns = [
    path("prueba/", views.PrubaView.as_view()),
    path("lista/", views.PruebaListView.as_view()),
    path("lista-prueba/", views.ListarPrueba.as_view()),
    path("add/", views.PruebaCreateView.as_view()),
]
    
    
