import os
from django.http import JsonResponse
from geo import settings
from geo.settings import BASE_DIR
import pandas as pd
from django.shortcuts import render

# Create your views here.
if settings.DEBUG:
    FILE_ROOT = os.path.join(BASE_DIR, 'test-files')
else:
    FILE_ROOT = os.path.join(BASE_DIR, 'files')

FILE_TMP = os.path.join(FILE_ROOT, 'tmp')


def municipios(request):
    return JsonResponse({"municipios":list_municipios()})


def categorias(request):
    return JsonResponse({"categorias":list_categorias()})


def list_municipios():
    pmv_csv = pd.read_csv(os.path.join(FILE_ROOT, 'pmv.csv'))
    df = pd.DataFrame(pmv_csv)
    _municipios = df['municipio'].unique()
    return _municipios.tolist()


def list_categorias():
    pmv_csv = pd.read_csv(os.path.join(FILE_ROOT, 'pmv.csv'))
    df = pd.DataFrame(pmv_csv)
    _subcategorias = df['subcategoria'].unique()
    return _subcategorias.tolist()


def filter_municipio_categoria(municipio_id, categoria):
    pmv_csv = pd.read_csv(os.path.join(FILE_ROOT, 'pmv.csv'))
    df = pd.DataFrame(pmv_csv)
    _municipios = df['municipio'] == municipio_id
    _subcategorias = df['subcategoria'] == categoria
    data = df[_municipios & _subcategorias]
    return data.set_index('categoria').T.to_dict()


def tables_merge(old, new, indicator):
    dfo = pd.read_csv(os.path.join(FILE_ROOT, old), encoding='ISO-8859-1')
    dfn = pd.read_csv(os.path.join(FILE_ROOT, new), encoding='ISO-8859-1')
    common_cols = list(dfo.columns.values)
    df = pd.merge(dfo, dfn, on=common_cols, how='outer', indicator=True)
    result = df[df['_merge'] == indicator]
    return result


def save_file(file):
    result = {}
    # path = FILE_TMP+'/%s' % file.name
    path = file.name
    print(path)
    with open(path, 'wb+') as dest:
                for chunk in file.chunks():
                    # print(chunk)
                    dest.write(chunk)
                result['path'] = path

    result['saved'] = True if os.path.exists(path) else False

    return result


def upload_file(request):
    message = ""
    if request.method == 'POST':
        if request.FILES['attachment']:
            file = request.FILES['attachment']
            with open(FILE_TMP+'/%s' % file.name, 'wb+') as dest:
                for chunk in file.chunks():
                    # print(chunk)
                    dest.write(chunk)
                message = "success"

    return JsonResponse({"result": message})