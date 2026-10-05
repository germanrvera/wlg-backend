from django.test import TestCase
from .models import FamiliaProducto, Proyecto


class FamiliaProductoTestCase(TestCase):
    def setUp(self):
        FamiliaProducto.objects.create(
            nombre='Sistemas de riel',
            descripcion='Familia de sistemas de riel premium',
            tipo='Sistemas de riel'
        )

    def test_familia_slug(self):
        familia = FamiliaProducto.objects.get(nombre='Sistemas de riel')
        self.assertEqual(familia.slug, 'sistemas-de-riel')


class ProyectoTestCase(TestCase):
    def setUp(self):
        Proyecto.objects.create(
            nombre='La Rural',
            descripcion='Proyecto premium',
            ubicacion='Buenos Aires',
            año=2024,
            tipo_espacio='Galerías'
        )

    def test_proyecto_slug(self):
        proyecto = Proyecto.objects.get(nombre='La Rural')
        self.assertEqual(proyecto.slug, 'la-rural')
