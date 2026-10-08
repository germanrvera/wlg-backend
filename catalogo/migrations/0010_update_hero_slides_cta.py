from django.db import migrations


UPDATES = [
    {'orden': 10, 'cta_url': '/familias/galuy'},
]


def update_slides(apps, schema_editor):
    HeroSlide = apps.get_model('catalogo', 'HeroSlide')
    for u in UPDATES:
        HeroSlide.objects.filter(orden=u['orden']).update(cta_url=u['cta_url'])


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0009_fix_heroslide_cta_url'),
    ]

    operations = [
        migrations.RunPython(update_slides, migrations.RunPython.noop),
    ]
