from django.core.management.base import BaseCommand
from catalogo.models import FamiliaProducto, Proyecto


class Command(BaseCommand):
    help = 'Carga datos iniciales de familias de productos y proyectos'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Cargando datos iniciales...'))

        # Familias de Productos
        familias_data = [
            {
                'nombre': 'Galuy',
                'tipo': 'Sistemas de riel',
                'descripcion': 'Sistema de riel premium con tecnología LED avanzada',
                'orden': 1
            },
            {
                'nombre': 'Cetus',
                'tipo': 'Sistemas de riel',
                'descripcion': 'Riel compacto para espacios arquitectónicos refinados',
                'orden': 2
            },
            {
                'nombre': 'Lira',
                'tipo': 'Sistemas de riel',
                'descripcion': 'Sistema flexible y modular para proyectos complejos',
                'orden': 3
            },
            {
                'nombre': 'Orion',
                'tipo': 'Sistemas de riel',
                'descripcion': 'Riel de precisión para iluminación especializada',
                'orden': 4
            },
            {
                'nombre': 'Petra',
                'tipo': 'Iluminación lineal',
                'descripcion': 'Luminaria lineal con acabado arquitectónico',
                'orden': 5
            },
            {
                'nombre': 'Sirio',
                'tipo': 'Iluminación lineal',
                'descripcion': 'Línea continua de luz con control inteligente',
                'orden': 6
            },
            {
                'nombre': 'Vega',
                'tipo': 'Iluminación lineal',
                'descripcion': 'Iluminación lineal de alto rendimiento',
                'orden': 7
            },
            {
                'nombre': 'Nova',
                'tipo': 'Sistemas especiales',
                'descripcion': 'Soluciones especiales para proyectos únicos',
                'orden': 8
            },
            {
                'nombre': 'Altair',
                'tipo': 'Sistemas especiales',
                'descripcion': 'Sistema de iluminación adaptable a medida',
                'orden': 9
            },
            {
                'nombre': 'Lyra',
                'tipo': 'Artefactos y apliques',
                'descripcion': 'Artefactos de diseño para espacios interiores',
                'orden': 10
            },
            {
                'nombre': 'Deneb',
                'tipo': 'Artefactos y apliques',
                'descripcion': 'Apliques decorativos con tecnología LED',
                'orden': 11
            },
            {
                'nombre': 'Castor',
                'tipo': 'Artefactos y apliques',
                'descripcion': 'Artefactos premium para acabados arquitectónicos',
                'orden': 12
            },
            {
                'nombre': 'Rigel',
                'tipo': 'Exterior',
                'descripcion': 'Iluminación exterior resistente y durable',
                'orden': 13
            },
            {
                'nombre': 'Mira',
                'tipo': 'Exterior',
                'descripcion': 'Sistema de iluminación para espacios externos',
                'orden': 14
            },
            {
                'nombre': 'Canopus',
                'tipo': 'Módulos',
                'descripcion': 'Módulos LED intercambiables y personalizables',
                'orden': 15
            },
            {
                'nombre': 'Pollux',
                'tipo': 'Módulos',
                'descripcion': 'Módulos de control y regulación inteligente',
                'orden': 16
            },
        ]

        for familia_data in familias_data:
            familia, created = FamiliaProducto.objects.get_or_create(
                nombre=familia_data['nombre'],
                defaults={
                    'tipo': familia_data['tipo'],
                    'descripcion': familia_data['descripcion'],
                    'orden': familia_data['orden'],
                    'imagen': 'familias/placeholder.jpg',
                }
            )
            if created:
                self.stdout.write(f'✓ Familia creada: {familia.nombre}')
            else:
                self.stdout.write(f'- Familia ya existe: {familia.nombre}')

        # Proyectos
        proyectos_data = [
            {
                'nombre': 'La Rural',
                'ubicacion': 'Buenos Aires',
                'año': 2024,
                'tipo_espacio': 'Galerías',
                'descripcion': 'Proyecto de iluminación arquitectónica para galerías de arte',
            },
            {
                'nombre': 'Movistar Arena VIP',
                'ubicacion': 'Buenos Aires',
                'año': 2024,
                'tipo_espacio': 'Entretenimiento',
                'descripcion': 'Iluminación premium para espacios VIP en arena de eventos',
            },
            {
                'nombre': 'Torre Bella',
                'ubicacion': 'Palermo, CABA',
                'año': 2023,
                'tipo_espacio': 'Residencial',
                'descripcion': 'Iluminación arquitectónica para torre residencial de lujo',
            },
            {
                'nombre': 'Parfumerie Recoleta',
                'ubicacion': 'Recoleta, CABA',
                'año': 2023,
                'tipo_espacio': 'Retail',
                'descripcion': 'Iluminación especializada para tienda de perfumería premium',
            },
            {
                'nombre': 'La Rando',
                'ubicacion': 'San Telmo, CABA',
                'año': 2022,
                'tipo_espacio': 'Gastronomía',
                'descripcion': 'Iluminación ambiental para restaurante de diseño',
            },
        ]

        for proyecto_data in proyectos_data:
            proyecto, created = Proyecto.objects.get_or_create(
                nombre=proyecto_data['nombre'],
                defaults={
                    'ubicacion': proyecto_data['ubicacion'],
                    'año': proyecto_data['año'],
                    'tipo_espacio': proyecto_data['tipo_espacio'],
                    'descripcion': proyecto_data['descripcion'],
                    'imagen_principal': 'proyectos/placeholder.jpg',
                }
            )
            if created:
                self.stdout.write(f'✓ Proyecto creado: {proyecto.nombre}')
            else:
                self.stdout.write(f'- Proyecto ya existe: {proyecto.nombre}')

        self.stdout.write(
            self.style.SUCCESS(
                '\n✓ Datos iniciales cargados correctamente'
            )
        )
