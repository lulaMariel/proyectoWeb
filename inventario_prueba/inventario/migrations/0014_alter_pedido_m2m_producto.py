# Generated by Django 5.1.3 on 2024-12-03 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0013_alter_pedido_m2m_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='m2m_producto',
            field=models.ManyToManyField(to='inventario.producto', verbose_name='Productos'),
        ),
    ]