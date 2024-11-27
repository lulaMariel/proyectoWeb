from django.urls import path
from .views import ProductoList

urlpatterns = [
    path('', ProductoList.as_view(), name='producto_list'),
]
