
from pickle import TRUE
from django.db import models
# Create your models here.
class Libro(models.Model):
    #id_cuenta = models.IntegerField()
    id_cuenta = models.ForeignKey(Cuenta, default=1, verbose_name="Cuenta", on_delete=models.SET_DEFAULT)
    fecha = models.DateField('Fecha:', auto_now=True, auto_now_add=False)
    nota = models.CharField('Nota Explicativa:', max_length=100, blank=True, editable=True)
    importe = models.DecimalField('Importe:', max_digits=18, decimal_places=2)
        
    def __str__(self):
       return str(self.id)  + ' - ' + self.nota
   
   