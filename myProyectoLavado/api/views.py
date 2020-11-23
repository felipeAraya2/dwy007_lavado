from django.shortcuts import render
from lavado.models import Producto
from .serializers import InsumosSerializer
from rest_framework import generics

# Create your views here.

class InsumosViewSet(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = InsumosSerializer

class InsumosFiltroNombreViewSet(generics.ListAPIView):
    serializer_class = InsumosSerializer
    def get_queryset(self):
        elnombre = self.kwargs['nombre']
        return Producto.objects.filter(nombre=elnombre)

class InsumosFiltroPrecioViewSet(generics.ListAPIView):
    serializer_class = InsumosSerializer
    def get_queryset (self):
        elprecio = self.kwargs['precio']
        return Producto.objects.filter(precio=elprecio)
