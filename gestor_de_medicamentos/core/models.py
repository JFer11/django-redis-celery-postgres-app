from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    document = models.CharField(max_length=9, unique=True)
    phone = models.CharField(max_length=9)
    sex = models.CharField(max_length=6, choices=[('MALE', 'Male'), ('FEMALE', 'Female')])

    def __str__(self):
        return f"{self.username} - {self.document}"


class Medicamento(models.Model):
    nombre = models.CharField(max_length=128)
    lote = models.CharField(max_length=128)
    cantidad_disponible = models.IntegerField()
    fecha_de_vencimiento = models.DateTimeField()
    cantidad_minima_del_medicamento = models.IntegerField()
    notificacion_previa_al_vencimiento = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} - Cantidad disponible: {self.cantidad_disponible} - Fecha de vencimiento: {self.fecha_de_vencimiento}"