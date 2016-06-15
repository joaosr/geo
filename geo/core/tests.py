from django.test import TestCase
from geo.core.models import Indice, Municipio
# Create your tests here.


class TestIndiceModel(TestCase):

    def setUp(self):
        self.municipio = Municipio(geocode='1100015',
                                   nome='Municipio1',
                                   estado='PA'
                                   )
        self.municipio.save()

    def test_simple_case(self):

        indice = Indice(
                        municipio=self.municipio,
                        indice=23.68,
                        categoria='PIB',
                        subcategoria='Imposto',
                        publicacao='2010-05-15')

        indice.save()
        self.assertTrue(Indice.objects.exists())
