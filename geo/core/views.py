import os
from django.http import JsonResponse
from geo.settings import BASE_DIR
import pandas as pd
from django.shortcuts import render

# Create your views here.
FILE_ROOT = os.path.join(BASE_DIR, 'files')

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

def is_new_table(old, new):
    csv_old = pd.read_csv(os.path.join(FILE_ROOT, old))
    csv_new = pd.read_csv(os.path.join(FILE_ROOT, new))
    dfo = pd.DataFrame(csv_old)
    dfn = pd.DataFrame(csv_new)
    common_cols = list(set(dfo.columns) & set(dfn.columns))
    #result = pd.merge(dfo, dfn, on=common_cols, how='inner')
    result = dfo.join(dfn, on=common_cols, how='inner')
    orows = len(dfo.index)
    rows = len(result.index)
    print(orows, rows)
    return False if rows > 0 else True
