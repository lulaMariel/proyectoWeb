# Generated by Django 5.1.3 on 2024-12-02 15:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0007_remove_pedido_nombre_producto_alter_pedido_fk_pedido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='entregado',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
