from django.db import migrations


SLIDES = [
    {
        'categoria': 'Lineal ARQ',
        'titulo': 'Galuy',
        'descripcion': 'Luz que acompaña el recorrido. Sistema de iluminación lineal diseñado para arquitecturas que demandan precisión y continuidad.',
        'cta_texto': 'Descubrir',
        'cta_url': '/familias/galuy',
        'photo': 'https://www.wlgled.com.ar/wp-content/uploads/2026/01/slider_galuy3.jpg',
        'alt': 'Galuy — Sistema Lineal ARQ',
        'orden': 10,
    },
    {
        'categoria': 'Sistema de riel',
        'titulo': 'Track LV',
        'descripcion': 'Sistema de iluminación en riel de bajo voltaje. Flexibilidad total para espacios comerciales y residenciales de alta gama.',
        'cta_texto': 'Descubrir',
        'cta_url': '/familias',
        'photo': 'https://www.wlgled.com.ar/wp-content/uploads/2025/12/tracklights_cover.prueba.jpg',
        'alt': 'Track LV — Sistema de Riel',
        'orden': 20,
    },
    {
        'categoria': 'Embutido magnético',
        'titulo': 'Micro\nRunner',
        'descripcion': 'Sistema de tamaño reducido para montaje embutido. Precisión óptica en el mínimo espacio posible.',
        'cta_texto': 'Descubrir',
        'cta_url': '/familias',
        'photo': 'https://www.wlgled.com.ar/wp-content/uploads/2025/12/cover_micro_runner7.prueba.jpg',
        'alt': 'Micro Runner — Embutido magnético',
        'orden': 30,
    },
    {
        'categoria': 'Lineal embutido',
        'titulo': 'Jenny\nX Pro',
        'descripcion': 'Lineal de máxima eficiencia para integración arquitectónica. Luz continua, sin interrupciones.',
        'cta_texto': 'Descubrir',
        'cta_url': '/familias',
        'photo': 'https://www.wlgled.com.ar/wp-content/uploads/2025/12/cover_jennyxpro.prueba-1.jpg',
        'alt': 'Jenny X Pro — Lineal embutido',
        'orden': 40,
    },
]


def load_slides(apps, schema_editor):
    HeroSlide = apps.get_model('catalogo', 'HeroSlide')
    for data in SLIDES:
        HeroSlide.objects.get_or_create(orden=data['orden'], defaults=data)


def unload_slides(apps, schema_editor):
    HeroSlide = apps.get_model('catalogo', 'HeroSlide')
    HeroSlide.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0007_heroslide'),
    ]

    operations = [
        migrations.RunPython(load_slides, unload_slides),
    ]
