# Generated by Django 5.1.3 on 2024-12-02 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0011_remove_pedido_fk_pedido_pedido_m2m_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='cantidad',
        ),
    ]
