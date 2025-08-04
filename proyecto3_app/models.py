from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    parentesco = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} ({self.edad} años) - ({self.parentesco})"

class Tienda(models.Model):
    descripcion = models.TextField()
    precio = models.FloatField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.descripcion} Precio: ${self.precio} - Cantidad: {self.cantidad}"