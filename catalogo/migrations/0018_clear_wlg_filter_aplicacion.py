from django.db import migrations

# Familias Powergear que ya tienen sus valores seteados en 0017
POWERGEAR = {'KIBUNI', 'GAN', 'DALI', 'KATAN', 'MODULOS', 'WALLY', 'MEMU', 'SAMAN', 'KUTZ', 'TAJAT'}


def clear_wlg_aplicacion(apps, schema_editor):
    FamiliaProducto = apps.get_model('catalogo', 'FamiliaProducto')
    FamiliaProducto.objects.exclude(nombre__in=POWERGEAR).update(filter_aplicacion=[])


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0017_set_filter_aplicacion'),
    ]

    operations = [
        migrations.RunPython(clear_wlg_aplicacion, noop),
    ]
