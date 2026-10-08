from django.db import migrations


FAMILIAS = [
    # Sistemas de riel
    {"nombre": "Galuy", "slug": "galuy", "tipo": "Sistema de Riel", "macro": "Sistemas de Riel", "orden": 10,
     "descripcion": "Sistema de riel monofásico de perfil bajo. Integración arquitectónica precisa para espacios residenciales y comerciales que exigen control lumínico dirigible con mínima presencia visual."},
    {"nombre": "Cetus", "slug": "cetus", "tipo": "Sistema de Riel", "macro": "Sistemas de Riel", "orden": 20,
     "descripcion": "Sistema de riel trifásico de alta capacidad. Permite la conexión simultánea de múltiples artefactos con gestión de circuitos independientes, ideal para showrooms y espacios de exposición."},
    {"nombre": "Lira", "slug": "lira", "tipo": "Sistema de Riel", "macro": "Sistemas de Riel", "orden": 30,
     "descripcion": "Sistema de riel empotrado de línea continua. Desaparece en el cielorraso generando una línea de luz dirigible que define el espacio sin interrumpir la pureza de la arquitectura."},
    {"nombre": "Orion", "slug": "orion", "tipo": "Sistema de Riel", "macro": "Sistemas de Riel", "orden": 40,
     "descripcion": "Sistema de riel magnético de bajo voltaje. Conexión y reposicionamiento sin herramientas para ambientes que requieren máxima flexibilidad en la composición lumínica."},
    # Iluminación lineal
    {"nombre": "Petra", "slug": "petra", "tipo": "Iluminación Lineal", "macro": "Iluminación Lineal", "orden": 50,
     "descripcion": "Perfil lineal de empotrar para iluminación de acento y ambient. Continuidad visual impecable en cielorrasos, nichos y detalles arquitectónicos que definen la identidad del espacio."},
    {"nombre": "Sirio", "slug": "sirio", "tipo": "Iluminación Lineal", "macro": "Iluminación Lineal", "orden": 60,
     "descripcion": "Perfil lineal de superficie con disipación térmica optimizada. Alta eficiencia lumínica en aplicaciones de iluminación general y decorativa para interiores de alto estándar."},
    {"nombre": "Vega", "slug": "vega", "tipo": "Iluminación Lineal", "macro": "Iluminación Lineal", "orden": 70,
     "descripcion": "Perfil lineal colgante de diseño suspendido. Elemento de iluminación y escultura que estructura el espacio verticalmente, compatible con configuraciones directas e indirectas."},
    # Sistemas especiales
    {"nombre": "Nova", "slug": "nova", "tipo": "Sistema Especial", "macro": "Sistemas Especiales", "orden": 80,
     "descripcion": "Sistema de iluminación modular para cielorrasos tensados y membranas translúcidas. Distribución lumínica uniforme con temperatura de color precisa para proyectos de diseño de alto impacto."},
    {"nombre": "Altair", "slug": "altair", "tipo": "Sistema Especial", "macro": "Sistemas Especiales", "orden": 90,
     "descripcion": "Sistema de iluminación perimetral para cornisas y remates arquitectónicos. Luz indirecta de alta calidad que amplifica volúmenes y define transiciones entre planos con sutileza técnica."},
    # Artefactos y apliques
    {"nombre": "Lyra", "slug": "lyra", "tipo": "Artefacto", "macro": "Artefactos y Apliques", "orden": 100,
     "descripcion": "Downlight de empotrar de perfil ultra-bajo. Integración total con el plano del cielorraso para iluminación de acento y general en residencias y locales comerciales premium."},
    {"nombre": "Deneb", "slug": "deneb", "tipo": "Artefacto", "macro": "Artefactos y Apliques", "orden": 110,
     "descripcion": "Aplique de pared de diseño arquitectónico. Iluminación decorativa y funcional para circulaciones, halls y espacios representativos donde la calidad de la luz construye atmósfera."},
    {"nombre": "Castor", "slug": "castor", "tipo": "Artefacto", "macro": "Artefactos y Apliques", "orden": 120,
     "descripcion": "Proyector de superficie orientable de alto rendimiento. Precisión focal para iluminación de obras de arte, vitrinas y elementos arquitectónicos que requieren control direccional exacto."},
    # Exterior
    {"nombre": "Rigel", "slug": "rigel", "tipo": "Exterior", "macro": "Exterior", "orden": 130,
     "descripcion": "Proyector exterior de alto rendimiento con protección IP65. Iluminación arquitectónica de fachadas, jardines y espacios públicos con eficiencia fotométrica certificada para entornos exigentes."},
    {"nombre": "Mira", "slug": "mira", "tipo": "Exterior", "macro": "Exterior", "orden": 140,
     "descripcion": "Luminaria empotrada de piso para exteriores con sellado IP67. Balizamiento y acento en pavimentos, escaleras y elementos de paisajismo con construcción robusta para uso permanente."},
    # Módulos
    {"nombre": "Canopus", "slug": "canopus", "tipo": "Módulo", "macro": "Módulos", "orden": 150,
     "descripcion": "Módulo LED de potencia variable para integración en sistemas de iluminación custom. Rendimiento lumínico de alta eficiencia con gestión térmica avanzada para instalaciones de diseño a medida."},
    {"nombre": "Pollux", "slug": "pollux", "tipo": "Módulo", "macro": "Módulos", "orden": 160,
     "descripcion": "Módulo LED regulable para sistemas de control DALI y 0-10V. Compatibilidad universal con protocolos de domótica para proyectos de arquitectura inteligente y control escénico avanzado."},
]


def load_familias(apps, schema_editor):
    FamiliaProducto = apps.get_model('catalogo', 'FamiliaProducto')
    for data in FAMILIAS:
        FamiliaProducto.objects.get_or_create(
            slug=data['slug'],
            defaults={
                'nombre': data['nombre'],
                'descripcion': data['descripcion'],
                'tipo': data['tipo'],
                'macro': data['macro'],
                'orden': data['orden'],
                'activo': True,
            }
        )


def unload_familias(apps, schema_editor):
    FamiliaProducto = apps.get_model('catalogo', 'FamiliaProducto')
    slugs = [f['slug'] for f in FAMILIAS]
    FamiliaProducto.objects.filter(slug__in=slugs).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0005_remove_producto_precio'),
    ]

    operations = [
        migrations.RunPython(load_familias, unload_familias),
    ]
