from django.contrib import admin
from .models import FamiliaProducto, Proyecto


@admin.register(FamiliaProducto)
class FamiliaProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo', 'orden', 'activo']
    list_filter = ['activo', 'tipo', 'creado']
    search_fields = ['nombre', 'descripcion']
    prepopulated_fields = {'slug': ('nombre',)}
    ordering = ['orden', 'nombre']
    fieldsets = (
        ('Información básica', {
            'fields': ('nombre', 'slug', 'tipo')
        }),
        ('Contenido', {
            'fields': ('descripcion', 'imagen')
        }),
        ('Configuración', {
            'fields': ('orden', 'activo')
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
