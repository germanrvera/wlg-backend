from rest_framework import viewsets, filters
from rest_framework.response import Response
from .models import FamiliaProducto, Proyecto, HeroSlide
from .serializers import FamiliaProductoSerializer, ProyectoSerializer, HeroSlideSerializer


class FamiliaProductoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FamiliaProducto.objects.filter(activo=True).order_by('orden')
    serializer_class = FamiliaProductoSerializer
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'tipo', 'descripcion']
    ordering_fields = ['orden', 'nombre']


class HeroSlideViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HeroSlide.objects.filter(activo=True).order_by('orden')
    serializer_class = HeroSlideSerializer


class ProyectoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Proyecto.objects.filter(activo=True).order_by('-año')
    serializer_class = ProyectoSerializer
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'ubicacion', 'tipo_espacio']
    ordering_fields = ['-año', 'nombre']
