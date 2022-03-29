
from django.db import models

# Create your models here.
class Cuenta(models.Model):
    nombre = models.CharField('Nombre', max_length=50, blank=True, editable=True)

    def __str__(self):
       return str(self.id)  + ' - ' + self.nombre
   
    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "nombres"

    def __str__(self):
        return self.nombres
    
    