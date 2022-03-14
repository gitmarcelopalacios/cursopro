from dataclasses import fields
from msilib.schema import ListView 
from pyexpat import model
from django.shortcuts import render

# Importo desde vistas genericas las vistas templates
from django.views.generic import (
    TemplateView, 
    ListView, 
    CreateView
)

from applications.home.models import Prueba 

# Las vistas genéricas TemplateView, 
# trabajan basadas en clases
class PrubaView(TemplateView):
    # le pasamos los parámetros para que esta
    # vista trabaje correctamente
    template_name = "home/prueba.html"
    
class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = "listaNumeros"
    queryset = ['0', '10', '20','30']

class ListarPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = 'lista'

class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    fields = ['titulo', 'subtitulo', 'cantidad']
  
