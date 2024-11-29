from django import forms
from .models import Producto, Pedido

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