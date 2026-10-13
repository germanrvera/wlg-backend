from django.db import migrations

APLICACION_MAP = {
    'KIBUNI':   ['Arquitectónico'],
    'GAN':      ['Arquitectónico', 'Comercial', 'Hospitality', 'Paisajismo', 'Residencial', 'Retail'],
    'DALI':     ['Comercial', 'Hospitality', 'Museos', 'Oficinas', 'Residencial', 'Retail'],
    'KATAN':    ['Comercial', 'Hospitality', 'Museos', 'Oficinas', 'Residencial', 'Retail'],
    'MODULOS':  ['Comercial', 'Hospitality', 'Museos', 'Oficinas', 'Residencial', 'Retail'],
    'WALLY':    ['Comercial', 'Decorativo', 'Hospitality', 'Oficinas', 'Residencial'],
    'MEMU':     ['Comercial', 'Hospitality', 'Oficinas', 'Residencial'],
    'SAMAN':    ['Paisajismo', 'Residencial'],
    'KUTZ':     ['Paisajismo', 'Residencial'],
    'TAJAT':    ['Paisajismo', 'Residencial'],
}


def set_filter_aplicacion(apps, schema_editor):
    FamiliaProducto = apps.get_model('catalogo', 'FamiliaProducto')
    for nombre, apps_list in APLICACION_MAP.items():
        FamiliaProducto.objects.filter(nombre__iexact=nombre).update(
            filter_aplicacion=apps_list
        )


def unset_filter_aplicacion(apps, schema_editor):
    FamiliaProducto = apps.get_model('catalogo', 'FamiliaProducto')
    for nombre in APLICACION_MAP:
        FamiliaProducto.objects.filter(nombre__iexact=nombre).update(
            filter_aplicacion=[]
        )


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0016_lanzamiento'),
    ]

    operations = [
        migrations.RunPython(set_filter_aplicacion, unset_filter_aplicacion),
    ]
