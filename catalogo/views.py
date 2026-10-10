from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FamiliaProducto, Proyecto, HeroSlide, Configuracion, Distribuidor, RecursoDescargable, Lanzamiento
from .serializers import FamiliaProductoSerializer, ProyectoSerializer, HeroSlideSerializer, DistribuidorSerializer, RecursoDescargableSerializer, LanzamientoSerializer


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


@api_view(['GET'])
def config_view(request):
    qs = Configuracion.objects.all()
    return Response({item.clave: item.valor for item in qs})


class DistribuidorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Distribuidor.objects.filter(activo=True)
    serializer_class = DistribuidorSerializer
    pagination_class = None


class RecursoDescargableViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RecursoDescargable.objects.filter(activo=True)
    serializer_class = RecursoDescargableSerializer
    pagination_class = None
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'familia', 'tipo']


class LanzamientoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lanzamiento.objects.filter(activo=True).order_by('orden')
    serializer_class = LanzamientoSerializer
    pagination_class = None


class ProyectoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Proyecto.objects.filter(activo=True).order_by('-año')
    serializer_class = ProyectoSerializer
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'ubicacion', 'tipo_espacio']
    ordering_fields = ['-año', 'nombre']
