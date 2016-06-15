from django.db import models
# from django.contrib.gis.db import models
#
# class WorldBorder(models.Model):
#     # Regular Django fields corresponding to the attributes in the
#     # world borders shapefile.
#     name = models.CharField(max_length=50)
#     area = models.IntegerField()
#     pop2005 = models.IntegerField('Population 2005')
#     fips = models.CharField('FIPS Code', max_length=2)
#     iso2 = models.CharField('2 Digit ISO', max_length=2)
#     iso3 = models.CharField('3 Digit ISO', max_length=3)
#     un = models.IntegerField('United Nations Code')
#     region = models.IntegerField('Region Code')
#     subregion = models.IntegerField('Sub-Region Code')
#     lon = models.FloatField()
#     lat = models.FloatField()
#
#     # GeoDjango-specific: a geometry field (MultiPolygonField)
#     mpoly = models.MultiPolygonField()
#
#     # Returns the string representation of the model.
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name

# Create your models here.


class Indice(models.Model):
    municipio = models.ForeignKey('Municipio', blank=True, null=True)
    indice = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    categoria = models.CharField('Categoria', max_length=100, blank=True, null=True)
    subcategoria = models.CharField('Subcategoria', max_length=100, blank=True, null=True)
    publicacao = models.DateField('Publicado', blank=True, null=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return str(self.indice)


class Municipio(models.Model):
    nome = models.CharField(max_length=60)
    geocode = models.CharField(max_length=7)
    estado = models.CharField(max_length=2, null=True)

    def __str__(self):
        return self.geocode
