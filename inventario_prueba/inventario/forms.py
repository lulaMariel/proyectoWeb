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
        widgets = {
            "numero_pedido": forms.NumberInput (attrs={
                'class': 'form-control',
                'placeholder': 'N° del producto',
            }),
            "nombre_cliente": forms.TextInput (attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del cliente',
            }),
            "fk_pedido": forms.Select (attrs={
                'class': 'form-control form-select',
            }),
            "cantidad": forms.NumberInput (attrs={
                'class': 'form-control',
                'placeholder': 'Cantidad del producto',
            }),
            "fecha": forms.DateInput (attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            "entregado": forms.CheckboxInput (attrs={
                'class': 'form-check-input form-bg-light',
                'type': 'checkbox',
            }),
        }