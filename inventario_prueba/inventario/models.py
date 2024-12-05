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
    producto = models.ManyToManyField(Producto, through = "DetallesPedido", verbose_name="Productos")

    def __str__(self):
        return (f"{self.nombre_cliente}")

class DetallesPedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete = models.CASCADE)
    cantidad = models.PositiveIntegerField(null=True, blank=True)
    precio = models.DecimalField(max_digits = 10, decimal_places = 2, null=True, blank=True)

    def __str__(self):
        return f"{self.producto} {self.cantidad} {self.precio}"