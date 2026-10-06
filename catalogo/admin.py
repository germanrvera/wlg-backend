from django.contrib import admin
from .models import FamiliaProducto, Proyecto


@admin.register(FamiliaProducto)
class FamiliaProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo', 'macro', 'skus', 'orden', 'activo']
    list_filter = ['activo', 'tipo', 'has_dim']
    search_fields = ['nombre', 'descripcion', 'macro']
    prepopulated_fields = {'slug': ('nombre',)}
    ordering = ['orden', 'nombre']
    fieldsets = (
        ('Información básica', {
            'fields': ('nombre', 'slug', 'tipo', 'macro', 'skus', 'orden', 'activo')
        }),
        ('Contenido', {
            'fields': ('descripcion', 'imagen', 'photo')
        }),
        ('Productos', {
            'fields': ('productos',),
            'description': 'Lista de SKUs/productos de esta familia (JSON array)'
        }),
        ('Filtros — Ubicación y aplicación', {
            'fields': ('filter_ubicacion', 'filter_aplicacion', 'filter_montaje'),
            'classes': ('collapse',),
        }),
        ('Filtros — Especificaciones técnicas', {
            'fields': ('filter_ct', 'filter_ip', 'filter_dim_sys', 'filter_cri',
                       'filter_v', 'filter_w', 'has_dim', 'w_range'),
            'classes': ('collapse',),
        }),
    )


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ubicacion', 'año', 'activo']
    list_filter = ['activo', 'año', 'tipo_espacio']
    search_fields = ['nombre', 'ubicacion', 'descripcion']
    prepopulated_fields = {'slug': ('nombre',)}
    ordering = ['-año', 'nombre']
    fieldsets = (
        ('Información básica', {
            'fields': ('nombre', 'slug', 'año')
        }),
        ('Ubicación y tipo', {
            'fields': ('ubicacion', 'tipo_espacio')
        }),
        ('Contenido', {
            'fields': ('descripcion', 'imagen_principal')
        }),
        ('Configuración', {
            'fields': ('activo',)
        }),
    )
