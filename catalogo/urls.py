from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FamiliaProductoViewSet, ProyectoViewSet, HeroSlideViewSet, DistribuidorViewSet, RecursoDescargableViewSet, config_view

router = DefaultRouter()
router.register(r'familias', FamiliaProductoViewSet, basename='familia')
router.register(r'proyectos', ProyectoViewSet, basename='proyecto')
router.register(r'hero-slides', HeroSlideViewSet, basename='heroslide')
router.register(r'distribuidores', DistribuidorViewSet, basename='distribuidor')
router.register(r'recursos', RecursoDescargableViewSet, basename='recurso')

urlpatterns = [
    path('', include(router.urls)),
    path('config/', config_view, name='config'),
]
