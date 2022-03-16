
from email.mime.image import MIMEImage
from django.db import models

# Importo la tabla departamento 
from applications.departamento.models import Departamento


# Create your models here.
class Empleado(models.Model):
    ''' Modelo para tabla empleado '''

    JOB_CHOICES = (
        ("0", "CONTADOR"),
        ("1", "ADMINISTRADOR"),
        ("2", "ECONOMISTA"),
        ("3", "OTRO"),
    )

    # Contador
    # Administrador
    # Economista
    # Otro
    
    first_name = models.CharField('Nombr(es)', max_length=60)
    last_name = models.CharField('Apellid(os)', max_length=60)
    # choices permite seleccionar entre diferentes opciones
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    # Foreignkey crea las relaciones
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
       return str(self.id)  + ' - ' + self.first_name + ' - ' + self.last_name