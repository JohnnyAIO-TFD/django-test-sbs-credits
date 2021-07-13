from django.db import models
# Create your models here.


class Clientes(models.Model):
    nombre = models.CharField(max_length=1000)
    dni = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre


class Creditos(models.Model):
    nombre = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    monto = models.FloatField(max_length=1000)
    aprobado = models.BooleanField(default="Null")


class SBS(models.Model):
    nombre = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    total = models.FloatField(max_length=1000)
