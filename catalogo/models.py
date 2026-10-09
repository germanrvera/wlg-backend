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


class HeroSlide(models.Model):
    categoria = models.CharField(max_length=60, help_text='Etiqueta pequeña encima del título')
    titulo = models.CharField(max_length=120, help_text='Título principal (\\n para salto de línea)')
    descripcion = models.CharField(max_length=300)
    cta_texto = models.CharField(max_length=60, default='Descubrir')
    cta_url = models.CharField(max_length=200, default='/familias')
    imagen = models.ImageField(upload_to='hero/', blank=True)
    photo = models.URLField(blank=True, help_text='URL externa (tiene prioridad sobre imagen subida)')
    alt = models.CharField(max_length=120, blank=True)
    orden = models.PositiveSmallIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['orden']
        verbose_name = 'Slide Hero'
        verbose_name_plural = 'Slides Hero'

    def __str__(self):
        return self.titulo


class Configuracion(models.Model):
    PAGINAS = [
        ('home', 'Home'),
        ('familias', 'Familias'),
        ('proyectos', 'Proyectos'),
        ('contacto', 'Contacto'),
        ('recursos', 'Recursos'),
        ('novedades', 'Novedades'),
        ('global', 'Global'),
    ]

    clave = models.SlugField(max_length=80, unique=True, help_text='Identificador interno. No cambiar.')
    valor = models.TextField(help_text='Texto visible. Podés usar <em>, <br> y <strong>.')
    descripcion = models.CharField(max_length=200, blank=True, help_text='Dónde aparece este texto en el sitio.')
    pagina = models.CharField(max_length=20, choices=PAGINAS, default='home')

    class Meta:
        verbose_name = 'Configuración de texto'
        verbose_name_plural = 'Configuración de textos'
        ordering = ['pagina', 'clave']

    def __str__(self):
        return f'{self.pagina} / {self.clave}'


class Distribuidor(models.Model):
    TIPOS = [('Oficial', 'Oficial'), ('Autorizado', 'Autorizado')]

    nombre = models.CharField(max_length=120)
    ciudad = models.CharField(max_length=80)
    zona = models.CharField(max_length=80, help_text='Provincia o región (para búsqueda)')
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=40, blank=True)
    url_mapa = models.URLField(blank=True, help_text='URL de Google Maps')
    tipo = models.CharField(max_length=20, choices=TIPOS, default='Autorizado')
    activo = models.BooleanField(default=True)
    orden = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = 'Distribuidor'
        verbose_name_plural = 'Distribuidores'
        ordering = ['zona', 'ciudad', 'orden', 'nombre']

    def __str__(self):
        return f'{self.ciudad} — {self.nombre}'


class RecursoDescargable(models.Model):
    TIPOS = [('IES', 'IES / Fotometría'), ('CAD', 'CAD / DWG'), ('PDF', 'PDF / Ficha técnica'), ('BIM', 'BIM / Revit')]

    nombre = models.CharField(max_length=200, help_text='Ej: Galuy — Fotometría 3000K 30°')
    familia = models.CharField(max_length=120, help_text='Nombre de la familia. Usar "General" para catálogos y guías.')
    tipo = models.CharField(max_length=10, choices=TIPOS)
    tamano = models.CharField(max_length=20, blank=True, help_text='Ej: 2.4 MB')
    archivo = models.FileField(upload_to='recursos/', blank=True, help_text='Se sube a R2 automáticamente.')
    url_externa = models.URLField(blank=True, help_text='URL directa (tiene prioridad sobre el archivo subido).')
    activo = models.BooleanField(default=True)
    orden = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = 'Recurso descargable'
        verbose_name_plural = 'Recursos descargables'
        ordering = ['familia', 'tipo', 'orden', 'nombre']

    def __str__(self):
        return f'{self.familia} — {self.nombre}'

    @property
    def url_descarga(self):
        if self.url_externa:
            return self.url_externa
        if self.archivo:
            return self.archivo.url
        return ''


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
