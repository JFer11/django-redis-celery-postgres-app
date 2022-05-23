from django.contrib import admin
from . import models

admin.site.site_header = 'Gestor de Medicamentos'
admin.site.register(models.User)
admin.site.register(models.Medicamento)
