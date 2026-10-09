from django.db import migrations


CONFIGS = [
    # HOME
    ('home', 'home_manifesto', 'Cada lumen tiene un lugar.<br>Nosotros lo encontramos.', 'Frase grande del manifiesto (home)'),
    ('home', 'home_stat_num', '200<sup>+</sup>', 'Número grande de la estadística (home)'),
    ('home', 'home_stat_label', 'Productos de iluminación LED profesional', 'Texto debajo del número (home)'),
    ('home', 'home_proyectos_titulo', 'Proyectos destacados', 'Título de la sección de proyectos (home)'),
    ('home', 'home_nl_titulo', 'Novedades para profesionales', 'Título del bloque de newsletter (home)'),
    # FAMILIAS
    ('familias', 'familias_page_titulo', 'Catálogo de <em>productos</em>', 'Título de la página de familias'),
    # PROYECTOS
    ('proyectos', 'proyectos_page_titulo', 'Cada espacio,<br>una <em>obra</em><br>de luz.', 'Título de la página de proyectos'),
    ('proyectos', 'proyectos_stat1_num', '+<em>120</em>', 'Número — stat 1 (proyectos)'),
    ('proyectos', 'proyectos_stat1_label', 'Proyectos', 'Etiqueta — stat 1 (proyectos)'),
    ('proyectos', 'proyectos_stat2_num', '<em>8</em>', 'Número — stat 2 (proyectos)'),
    ('proyectos', 'proyectos_stat2_label', 'Ciudades', 'Etiqueta — stat 2 (proyectos)'),
    ('proyectos', 'proyectos_stat3_num', '+<em>40</em>', 'Número — stat 3 (proyectos)'),
    ('proyectos', 'proyectos_stat3_label', 'Estudios', 'Etiqueta — stat 3 (proyectos)'),
    # CONTACTO
    ('contacto', 'contacto_page_titulo', 'Hablemos de<br>tu <em>proyecto</em>.', 'Título de la página de contacto'),
    ('contacto', 'contacto_direccion', 'Av. Corrientes 1234, Piso 8<br>CABA, Buenos Aires', 'Dirección física'),
    ('contacto', 'contacto_horario', 'Lunes a Viernes<br>9:00 – 18:00 hs', 'Horario de atención'),
    # RECURSOS
    ('recursos', 'recursos_page_titulo', 'Herramientas para<br>el <em>proyectista</em>.', 'Título de la página de recursos'),
    # NOVEDADES
    ('novedades', 'novedades_page_titulo', 'Noticias, <em>anuncios</em><br>y lanzamientos.', 'Título de la página de novedades'),
]


def load_configs(apps, schema_editor):
    Configuracion = apps.get_model('catalogo', 'Configuracion')
    for pagina, clave, valor, descripcion in CONFIGS:
        Configuracion.objects.get_or_create(
            clave=clave,
            defaults={'pagina': pagina, 'valor': valor, 'descripcion': descripcion}
        )


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0011_configuracion'),
    ]

    operations = [
        migrations.RunPython(load_configs, migrations.RunPython.noop),
    ]
