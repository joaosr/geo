from django.test import TestCase
from geo.core.models import Indice
# Create your tests here.


class TestIndiceModel(TestCase):
    def test_simple_case(self):
        indice = Indice(
            municipio=1505555,
            indice=23.68,
            categoria="PIB",
            subcategoria="Imposto",
            publicacao="2010-05-15",
        )

        indice.save()
        self.assertTrue(Indice.objects.exists())
