from django import forms
from .models import Producto, Pedido
from datetime import date

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            "nombre": forms.TextInput (attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del producto',
            }),
            "categoria": forms.TextInput (attrs={
                'class': 'form-control',
                'placeholder': 'Categoria del producto',
            }),
            "precio": forms.NumberInput (attrs={
                'class': 'form-control',
                'placeholder': 'Precio del producto',
            }),
            "stock": forms.NumberInput (attrs={
                'class': 'form-control',
                'placeholder': 'Stock del producto',
            }),
        }

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
        widgets = {
            "numero_pedido": forms.NumberInput (attrs={
                'class': 'form-control',
                'placeholder': 'N° del producto',
            }),
            "nombre_cliente": forms.TextInput (attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del cliente',
            }),
            "fecha": forms.DateInput (attrs={
                'class': 'form-control',
                'type': 'date',
                'value': date.today().strftime('%Y-%m-%d'),
            }),
            "entregado": forms.Select(choices=[(None, ""), (True, "Sí"), (False, "No"),], attrs={
                    'class': 'form-control form-select',
                }
            ),
            "m2m_producto": forms.CheckboxSelectMultiple (attrs={
                'class': 'form-checkbox-input',
            }),
        }