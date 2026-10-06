from rest_framework import serializers
from .models import FamiliaProducto, Proyecto


class FamiliaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamiliaProducto
        fields = [
            'id', 'nombre', 'slug', 'descripcion', 'imagen', 'photo',
            'tipo', 'macro', 'skus', 'orden',
            'filter_ct', 'filter_ip', 'filter_dim_sys', 'filter_cri',
            'filter_v', 'filter_w', 'filter_ubicacion', 'filter_aplicacion',
            'filter_montaje', 'has_dim', 'w_range', 'productos',
        ]


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = [
            'id', 'nombre', 'slug', 'descripcion', 'ubicacion', 'año', 'tipo_espacio',
            'imagen_principal', 'lead', 'quote', 'quote_autor',
            'galeria', 'bloques', 'ficha_tecnica',
        ]
