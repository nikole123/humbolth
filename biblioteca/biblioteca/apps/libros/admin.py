from django.contrib import admin
from biblioteca.apps.libros.models import *

admin.site.register(Espacio)
admin.site.register(Usuario)
admin.site.register(Tipo_Usuario)
admin.site.register(Prestamo)
admin.site.register(Bibliotecario)