from django.db import models
from django.utils.text import slugify


class FamiliaProducto(models.Model):
    nombre = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='familias/', blank=True)
    photo = models.URLField(blank=True)
    tipo = models.CharField(max_length=60)
    macro = models.CharField(max_length=60, blank=True)
    skus = models.PositiveSmallIntegerField(default=0)
    orden = models.PositiveSmallIntegerField(default=0)
    activo = models.BooleanField(default=True)

    # Filter fields
    filter_ct = models.JSONField(default=list)
    filter_ip = models.JSONField(default=list)
    filter_dim_sys = models.JSONField(default=list)
    filter_cri = models.JSONField(default=list)
    filter_v = models.JSONField(default=list)
    filter_w = models.JSONField(default=list)
    filter_ubicacion = models.JSONField(default=list)
    filter_aplicacion = models.JSONField(default=list)
    filter_montaje = models.JSONField(default=list)
    has_dim = models.BooleanField(default=False)
    w_range = models.JSONField(default=list)

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Familia de Producto'
        verbose_name_plural = 'Familias de Productos'
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)


class Producto(models.Model):
    familia = models.ForeignKey(
        FamiliaProducto, on_delete=models.CASCADE,
        related_name='items', verbose_name='Familia'
    )
    codigo = models.CharField(max_length=80, unique=True, verbose_name='Código SKU')
    descripcion = models.CharField(max_length=250, verbose_name='Descripción')
    imagen = models.ImageField(upload_to='productos/', blank=True, verbose_name='Imagen')
    activo = models.BooleanField(default=True)
    orden = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['familia__orden', 'orden', 'codigo']

    def __str__(self):
        return self.codigo


class Proyecto(models.Model):
    nombre = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=120)
    año = models.PositiveSmallIntegerField()
    tipo_espacio = models.CharField(max_length=80)
    imagen_principal = models.ImageField(upload_to='proyectos/')
    activo = models.BooleanField(default=True)

    # Detalle de proyecto
    lead = models.TextField(blank=True, help_text='Párrafo introductorio largo')
    quote = models.CharField(max_length=300, blank=True)
    quote_autor = models.CharField(max_length=120, blank=True)
    galeria = models.JSONField(default=list, help_text='Lista de URLs de imágenes de la galería')
    bloques = models.JSONField(default=list, help_text='Lista de {num, title, img, text}')
    ficha_tecnica = models.JSONField(default=dict, help_text='Dict de {clave: valor} — lighting designer, comercializador, etc.')

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-año', '-creado']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)
