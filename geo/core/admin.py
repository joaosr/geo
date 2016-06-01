# from django.contrib.gis import admin
# from .models import WorldBorder
#
# admin.site.register(WorldBorder, admin.GeoModelAdmin)
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from geo.core.models import Indice


class IndiceResource(resources.ModelResource):

    class Meta:
        model = Indice
        fields = ('municipio', 'indice', 'categoria', 'subcategoria', 'publicacao',)


class IndiceAdmin(ImportExportModelAdmin):

    class Meta:
        model = Indice
        fields = ('municipio', 'indice', 'categoria', 'subcategoria', 'publicacao',)

admin.site.register(Indice,IndiceAdmin)