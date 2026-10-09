from rest_framework import serializers
from .models import FamiliaProducto, Producto, Proyecto, HeroSlide, Configuracion, Distribuidor


class ProductoSerializer(serializers.ModelSerializer):
    cod = serializers.CharField(source='codigo')
    desc = serializers.CharField(source='descripcion')

    class Meta:
        model = Producto
        fields = ['cod', 'desc', 'imagen']


class FamiliaProductoSerializer(serializers.ModelSerializer):
    productos = serializers.SerializerMethodField()
    skus = serializers.SerializerMethodField()

    class Meta:
        model = FamiliaProducto
        fields = [
            'id', 'nombre', 'slug', 'descripcion', 'imagen', 'photo',
            'tipo', 'macro', 'skus', 'orden',
            'filter_ct', 'filter_ip', 'filter_dim_sys', 'filter_cri',
            'filter_v', 'filter_w', 'filter_ubicacion', 'filter_aplicacion',
            'filter_montaje', 'has_dim', 'w_range', 'productos',
        ]

    def get_productos(self, obj):
        qs = obj.items.filter(activo=True).order_by('orden', 'codigo')
        return ProductoSerializer(qs, many=True).data

    def get_skus(self, obj):
        return obj.items.filter(activo=True).count()


class HeroSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSlide
        fields = ['id', 'categoria', 'titulo', 'descripcion', 'cta_texto', 'cta_url',
                  'imagen', 'photo', 'alt', 'orden']


class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracion
        fields = ['clave', 'valor']


class DistribuidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distribuidor
        fields = ['nombre', 'ciudad', 'zona', 'direccion', 'telefono', 'url_mapa', 'tipo']


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = [
            'id', 'nombre', 'slug', 'descripcion', 'ubicacion', 'año', 'tipo_espacio',
            'imagen_principal', 'lead', 'quote', 'quote_autor',
            'galeria', 'bloques', 'ficha_tecnica',
        ]
