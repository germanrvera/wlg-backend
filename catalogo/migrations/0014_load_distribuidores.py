from django.db import migrations


DISTRIBUIDORES = [
    # (nombre, ciudad, zona, direccion, telefono, url_mapa, tipo, orden)
    ('WLG Store Palermo', 'Buenos Aires', 'CABA', 'Thames 1830, Palermo', '+54 11 4833-2200', 'https://maps.google.com/?q=Thames+1830+Palermo+Buenos+Aires', 'Oficial', 1),
    ('Luminotecnia Belgrano', 'Buenos Aires', 'CABA', 'Av. Cabildo 2150, Belgrano', '+54 11 4786-1100', 'https://maps.google.com/?q=Av+Cabildo+2150+Belgrano+Buenos+Aires', 'Autorizado', 2),
    ('WLG San Isidro', 'Buenos Aires', 'GBA Norte', 'Av. Centenario 450, San Isidro', '+54 11 4732-5500', 'https://maps.google.com/?q=Av+Centenario+450+San+Isidro', 'Autorizado', 1),
    ('Luz Arquitectónica Cba', 'Córdoba', 'Córdoba', 'Av. Colón 450, Nueva Córdoba', '+54 351 422-1800', 'https://maps.google.com/?q=Av+Colon+450+Cordoba', 'Oficial', 1),
    ('Iluminar Cba', 'Córdoba', 'Córdoba', 'Av. Hipólito Yrigoyen 312', '+54 351 469-3300', 'https://maps.google.com/?q=Av+Hipolito+Yrigoyen+312+Cordoba', 'Autorizado', 2),
    ('Iluminación Profesional Sur', 'Rosario', 'Santa Fe', 'Av. Pellegrini 1200, Rosario', '+54 341 449-7700', 'https://maps.google.com/?q=Av+Pellegrini+1200+Rosario', 'Oficial', 1),
    ('WLG Cuyo', 'Mendoza', 'Mendoza', 'Av. San Martín 890, Ciudad', '+54 261 420-6600', 'https://maps.google.com/?q=Av+San+Martin+890+Mendoza', 'Oficial', 1),
    ('Lux Arquitectura NOA', 'Tucumán', 'Tucumán', 'Maipú 760, San Miguel de Tucumán', '+54 381 430-1200', 'https://maps.google.com/?q=Maipu+760+Tucuman', 'Autorizado', 1),
    ('Distribuidora Norte LED', 'Salta', 'Salta', 'Balcarce 550, Salta Capital', '+54 387 422-4400', 'https://maps.google.com/?q=Balcarce+550+Salta', 'Autorizado', 1),
    ('Ílux Santa Fe', 'Santa Fe', 'Santa Fe', 'Bv. Gálvez 1100, Santa Fe', '+54 342 460-8800', 'https://maps.google.com/?q=Bv+Galvez+1100+Santa+Fe', 'Autorizado', 2),
    ('Costa Luz LED', 'Mar del Plata', 'Buenos Aires', 'Av. Colón 3500, Mar del Plata', '+54 223 495-2200', 'https://maps.google.com/?q=Av+Colon+3500+Mar+del+Plata', 'Autorizado', 1),
    ('Patagonia Ilumina', 'Neuquén', 'Patagonia', 'Av. Argentina 560, Neuquén', '+54 299 447-3300', 'https://maps.google.com/?q=Av+Argentina+560+Neuquen', 'Autorizado', 1),
]


def load_distribuidores(apps, schema_editor):
    Distribuidor = apps.get_model('catalogo', 'Distribuidor')
    for nombre, ciudad, zona, direccion, telefono, url_mapa, tipo, orden in DISTRIBUIDORES:
        Distribuidor.objects.get_or_create(
            nombre=nombre,
            ciudad=ciudad,
            defaults={
                'zona': zona,
                'direccion': direccion,
                'telefono': telefono,
                'url_mapa': url_mapa,
                'tipo': tipo,
                'orden': orden,
            }
        )


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0013_distribuidor'),
    ]

    operations = [
        migrations.RunPython(load_distribuidores, migrations.RunPython.noop),
    ]
