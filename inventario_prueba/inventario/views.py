from django.shortcuts import render
from django.views.generic import ListView
from .models import Producto

class ProductoList(ListView):
    model = Producto