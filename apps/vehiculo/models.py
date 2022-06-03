from django.db import models

# Create your models here.


class Marca(models.Model):
    nombre = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = 'marca'
        ordering = ['id']


class TipoVehiculo(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = 'tipo_Vehiculo'
        ordering = ['id']


class Vehiculo(models.Model):
    modelo = models.CharField(max_length=30)
    color = models.CharField(max_length=20)
    placa = models.CharField(max_length=15)
    motor = models.CharField(max_length=10)
    marca = models.ForeignKey(
        Marca, null=True, blank=True, on_delete=models.CASCADE)
    tipoVehiculo = models.ForeignKey(
        TipoVehiculo, null=True, blank=True, on_delete=models.CASCADE,verbose_name="Tipo de Vehiculo")

    def __str__(self) -> str:
        return self.modelo

    class Meta:
        verbose_name = 'vehiculo'
        ordering = ['id']