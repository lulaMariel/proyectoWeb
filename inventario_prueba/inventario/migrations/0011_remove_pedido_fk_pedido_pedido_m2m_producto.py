# Generated by Django 5.1.3 on 2024-12-02 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0010_remove_pedido_fk_pedido_pedido_fk_pedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='fk_pedido',
        ),
        migrations.AddField(
            model_name='pedido',
            name='m2m_producto',
            field=models.ManyToManyField(to='inventario.producto', verbose_name='Productos'),
        ),
    ]
