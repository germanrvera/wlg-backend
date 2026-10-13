from django.db import migrations

POWERGEAR = {'KIBUNI', 'GAN', 'DALI', 'KATAN', 'MODULOS', 'WALLY', 'MEMU', 'SAMAN', 'KUTZ', 'TAJAT'}


def remove_mesa(apps, schema_editor):
    FamiliaProducto = apps.get_model('catalogo', 'FamiliaProducto')
    for familia in FamiliaProducto.objects.exclude(nombre__in=POWERGEAR):
        if familia.filter_aplicacion and 'Mesa' in familia.filter_aplicacion:
            familia.filter_aplicacion = [v for v in familia.filter_aplicacion if v != 'Mesa']
            familia.save(update_fields=['filter_aplicacion'])


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0017_set_filter_aplicacion'),
    ]

    operations = [
        migrations.RunPython(remove_mesa, noop),
    ]
