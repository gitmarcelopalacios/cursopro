from django.contrib import admin
from .models import Libro
from .models import Cuenta

admin.site.register(Libro)
admin.site.register(Cuenta)
