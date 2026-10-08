from django.db import migrations


def fix_cta_urls(apps, schema_editor):
    HeroSlide = apps.get_model('catalogo', 'HeroSlide')
    HeroSlide.objects.filter(cta_url='/familias/galuy').update(cta_url='/familias')


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0008_load_hero_slides'),
    ]

    operations = [
        migrations.RunPython(fix_cta_urls, migrations.RunPython.noop),
    ]
