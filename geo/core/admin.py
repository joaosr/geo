# from django.contrib.gis import admin
# from .models import WorldBorder
#
# admin.site.register(WorldBorder, admin.GeoModelAdmin)
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export import fields
from geo.core.models import Indice, Municipio
from import_export.widgets import ForeignKeyWidget


class IndiceResource(resources.ModelResource):
    municipio = fields.Field(
        column_name='municipio',
        attribute='municipio',
        widget=ForeignKeyWidget(Municipio, 'geocode'))

    class Meta:
        model = Indice
        fields = ('municipio', 'indice', 'categoria', 'subcategoria', 'publicacao',)


class IndiceAdmin(ImportExportModelAdmin):

    class Meta:
        resource_class = IndiceResource

admin.site.register(Indice, IndiceAdmin)


class MunicipioAdmin(ImportExportModelAdmin):
    list_display = ('nome', 'geocode', 'estado')
    search_fields = ('nome', 'geocode', 'estado')

    class Meta:
        model = Municipio
        fields = ('nome', 'geocode', 'estado')

admin.site.register(Municipio, MunicipioAdmin)
