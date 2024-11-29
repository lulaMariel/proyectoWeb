from django.db import models

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
    nombre_producto = models.CharField(max_length = 100)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField(default = False)
    fk_pedido = models.ForeignKey(Producto, on_delete = models.PROTECT, verbose_name="Pedido")

    def __str__(self):
        return (f"{self.nombre_cliente}")