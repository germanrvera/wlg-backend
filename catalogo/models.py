from django.db import models
from django.utils.text import slugify


class FamiliaProducto(models.Model):
    nombre = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='familias/')
    tipo = models.CharField(max_length=60)  # ej: "Sistemas de riel"
    orden = models.PositiveSmallIntegerField(default=0)
    activo = models.BooleanField(default=True)
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


class Proyecto(models.Model):
    nombre = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=120)
    año = models.PositiveSmallIntegerField()
    tipo_espacio = models.CharField(max_length=80)
    imagen_principal = models.ImageField(upload_to='proyectos/')
    activo = models.BooleanField(default=True)
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
