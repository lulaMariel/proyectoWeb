from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Producto
from .forms import ProductoForm

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