from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Producto, Pedido
from .forms import ProductoForm, PedidoForm

# Productos

class InicioView(TemplateView):
    model = Producto
    template_name = 'inicio_view.html'

class ProductoListView(ListView):
    model = Producto
    success_url= reverse_lazy('producto_list')

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    success_url= reverse_lazy('producto_list')

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    success_url= reverse_lazy('producto_list')

class ProductoDeleteView(DeleteView):
    model = Producto
    success_url= reverse_lazy('producto_list')

# Pedidos

class PedidoListView(ListView):
    model = Pedido

class PedidoCreateView(CreateView):
    model = Pedido
    form_class = PedidoForm
    success_url = reverse_lazy('pedido_list')

    def form_valid(self, form):
        pedido = form.save()  # Guardar el pedido

        # Django maneja la relación ManyToMany automáticamente
        productos_seleccionados = form.cleaned_data['producto']
        pedido.producto.set(productos_seleccionados)  # Establecer los productos seleccionados

        return super().form_valid(form)

class PedidoUpdateView(UpdateView):
    model = Pedido
    form_class = PedidoForm
    success_url = reverse_lazy('pedido_list')

class PedidoDeleteView(DeleteView):
    model = Pedido
    success_url = reverse_lazy('pedido_list')