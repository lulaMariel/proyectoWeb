from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Producto
from .forms import ProductoForm

class ProductoListView(ListView):
    model = Producto

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