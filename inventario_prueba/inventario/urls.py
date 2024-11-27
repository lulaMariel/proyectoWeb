from django.urls import path
from .views import ProductoListView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView

urlpatterns = [
    path('', ProductoListView.as_view(), name='producto_list'),
    path('agregar/', ProductoCreateView.as_view(), name='producto_create'),
    path('modificar/<pk>', ProductoUpdateView.as_view(), name='producto_update'),
    path('eliminar/<pk>', ProductoDeleteView.as_view(), name='producto_delete'),
]
