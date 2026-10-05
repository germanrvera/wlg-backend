from rest_framework import serializers
from .models import FamiliaProducto, Proyecto


class FamiliaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamiliaProducto
        fields = ['id', 'nombre', 'slug', 'descripcion', 'imagen', 'tipo', 'orden']


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ['id', 'nombre', 'slug', 'descripcion', 'ubicacion', 'año', 'tipo_espacio', 'imagen_principal']
