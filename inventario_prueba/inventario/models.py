from django.db import models
from datetime import date

class Producto(models.Model):
    nombre = models.CharField(max_length = 100)
    categoria = models.CharField(max_length = 50)
    precio = models.DecimalField(max_digits = 10, decimal_places = 2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return (f"{self.nombre}")

class Pedido(models.Model):
    numero_pedido = models.PositiveIntegerField(verbose_name="Número pedido")
    nombre_cliente = models.CharField(max_length = 100)
    fecha = models.DateField()
    entregado = models.BooleanField(null=True, blank=True)
    m2m_producto = models.ManyToManyField(Producto, verbose_name="Productos")

    def __str__(self):
        return (f"{self.nombre_cliente}")