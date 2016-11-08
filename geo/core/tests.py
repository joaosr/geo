from django.test import TestCase
from geo.core.models import Indice, Municipio
from geo.core.views import list_municipios, list_categorias, filter_municipio_categoria, tables_merge
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

    def test_list_municipios(self):
        self.assertTrue(1500107 in list_municipios())

    def test_list_categorias(self):
        self.assertTrue('Acesso à água' in list_categorias())

    def test_filter_municipio_categoria(self):
        filtro = filter_municipio_categoria(1500107, 'Acesso à água')
        self.assertTrue('Industrial' in filtro.keys())

    def test_filter_municipio_categoria(self):
        filtro = filter_municipio_categoria(1500107, 'Acesso à água')
        self.assertTrue('Industrial' in filtro.keys())

    def test_table_has_new_entries(self):
        new_table = tables_merge('bolsa_familia_ate_2011.csv', 'bolsa_familia_2012.csv', 'left_only')
        self.assertTrue(len(new_table.index) > 0)

    def test_table_has_not_new_entries(self):
        new_table = tables_merge('bolsa_familia_ate_2011.csv', 'bolsa_familia_2008.csv', 'both')
        self.assertTrue(len(new_table.index) > 0)


