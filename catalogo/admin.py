from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from .models import FamiliaProducto, Producto, Proyecto, HeroSlide, Configuracion, Distribuidor, RecursoDescargable


class ProductoResource(resources.ModelResource):
    familia = fields.Field(
        column_name='familia',
        attribute='familia',
        widget=ForeignKeyWidget(FamiliaProducto, 'nombre')
    )

    class Meta:
        model = Producto
        import_id_fields = ['codigo']
        fields = ['familia', 'codigo', 'descripcion', 'orden', 'activo']
        export_order = ['familia', 'codigo', 'descripcion', 'orden', 'activo']


class ProductoInline(admin.TabularInline):
    model = Producto
    extra = 0
    fields = ['codigo', 'descripcion', 'imagen', 'orden', 'activo']
    ordering = ['orden', 'codigo']


@admin.register(Producto)
class ProductoAdmin(ImportExportModelAdmin):
    resource_classes = [ProductoResource]
    list_display = ['codigo', 'descripcion', 'familia', 'activo']
    list_filter = ['activo', 'familia__tipo', 'familia']
    search_fields = ['codigo', 'descripcion']
    list_editable = ['activo']
    ordering = ['familia__orden', 'orden', 'codigo']


@admin.register(FamiliaProducto)
class FamiliaProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo', 'macro', 'orden', 'activo']
    list_filter = ['activo', 'tipo', 'has_dim']
    search_fields = ['nombre', 'descripcion', 'macro']
    prepopulated_fields = {'slug': ('nombre',)}
    ordering = ['orden', 'nombre']
    inlines = [ProductoInline]
    fieldsets = (
        ('Información básica', {
            'fields': ('nombre', 'slug', 'tipo', 'macro', 'orden', 'activo')
        }),
        ('Contenido', {
            'fields': ('descripcion', 'imagen', 'photo')
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


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria', 'orden', 'activo']
    list_editable = ['orden', 'activo']
    ordering = ['orden']
    fieldsets = (
        ('Contenido', {
            'fields': ('categoria', 'titulo', 'descripcion', 'cta_texto', 'cta_url')
        }),
        ('Imagen', {
            'fields': ('imagen', 'photo', 'alt'),
            'description': 'photo (URL externa) tiene prioridad. Si no hay URL, se usa la imagen subida.'
        }),
        ('Configuración', {
            'fields': ('orden', 'activo')
        }),
    )


@admin.register(Configuracion)
class ConfiguracionAdmin(admin.ModelAdmin):
    list_display = ['pagina', 'clave', 'valor_preview', 'descripcion']
    list_filter = ['pagina']
    search_fields = ['clave', 'valor', 'descripcion']
    ordering = ['pagina', 'clave']
    readonly_fields = ['clave']
    fields = ['pagina', 'clave', 'descripcion', 'valor']

    def valor_preview(self, obj):
        return obj.valor[:60] + '...' if len(obj.valor) > 60 else obj.valor
    valor_preview.short_description = 'Valor'


@admin.register(Distribuidor)
class DistribuidorAdmin(admin.ModelAdmin):
    list_display = ['ciudad', 'nombre', 'zona', 'tipo', 'telefono', 'activo', 'orden']
    list_filter = ['activo', 'tipo', 'zona']
    list_editable = ['activo', 'orden']
    search_fields = ['nombre', 'ciudad', 'zona', 'direccion']
    ordering = ['zona', 'ciudad', 'orden']
    fieldsets = (
        ('Identificación', {
            'fields': ('nombre', 'tipo', 'activo', 'orden')
        }),
        ('Ubicación', {
            'fields': ('ciudad', 'zona', 'direccion', 'url_mapa')
        }),
        ('Contacto', {
            'fields': ('telefono',)
        }),
    )


@admin.register(RecursoDescargable)
class RecursoDescargableAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'familia', 'tipo', 'tamano', 'activo', 'orden']
    list_filter = ['activo', 'tipo', 'familia']
    list_editable = ['activo', 'orden']
    search_fields = ['nombre', 'familia']
    ordering = ['familia', 'tipo', 'orden']
    fieldsets = (
        ('Identificación', {
            'fields': ('nombre', 'familia', 'tipo', 'tamano', 'activo', 'orden')
        }),
        ('Archivo', {
            'fields': ('archivo', 'url_externa'),
            'description': 'url_externa tiene prioridad. Si no hay URL, se usa el archivo subido (va a R2).'
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
            'fields': ('nombre', 'slug', 'año', 'ubicacion', 'tipo_espacio', 'activo')
        }),
        ('Imágenes', {
            'fields': ('imagen_principal', 'galeria'),
            'description': 'galeria: lista de URLs ["url1", "url2", ...]'
        }),
        ('Texto', {
            'fields': ('descripcion', 'lead', 'quote', 'quote_autor')
        }),
        ('Bloques narrativos', {
            'fields': ('bloques',),
            'classes': ('collapse',),
            'description': 'Lista de [{num, title, img, text}]'
        }),
        ('Ficha técnica', {
            'fields': ('ficha_tecnica',),
            'classes': ('collapse',),
            'description': 'Dict de {Clave: Valor}'
        }),
    )
