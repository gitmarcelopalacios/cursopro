from msilib.schema import ListView
from django.shortcuts import render

# Importo desde vistas genericas las vistas templates
from django.views.generic import TemplateView, ListView 

# Las vistas genéricas TemplateView, 
# trabajan basadas en clases
class PrubaView(TemplateView):
    # le pasamos los parámetros para que esta
    # vista trabaje correctamente
    template_name = "home/prueba.html"
    
class PruebaListView(ListView):
    template_name = "home/lista.html"
    queryset = ['0', '10', '20','30']

