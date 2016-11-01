from django.http import JsonResponse
import pandas as pd
from django.shortcuts import render

# Create your views here.

def municipios(request):
    return JsonResponse({"municipios":list_municipios()})

def categorias(request):
    return JsonResponse({"categorias":list_categorias()})

def list_municipios():
    pmv_csv = pd.read_csv('/home/joaosr/Desenvolvimento/geo/geo/core/pmv.csv')
    df = pd.DataFrame(pmv_csv)
    _municipios = df['municipio'].unique()
    return _municipios.tolist()

def list_categorias():
    pmv_csv = pd.read_csv('/home/joaosr/Desenvolvimento/geo/geo/core/pmv.csv')
    df = pd.DataFrame(pmv_csv)
    _subcategorias = df['subcategoria'].unique()
    return _subcategorias.tolist()

def filter_municipio_categoria(municipio_id, categoria):
    pmv_csv = pd.read_csv('/home/joaosr/Desenvolvimento/geo/geo/core/pmv.csv')
    df = pd.DataFrame(pmv_csv)
    _municipios = df['municipio'] == municipio_id
    _subcategorias = df['subcategoria'] == categoria
    data = df[_municipios & _subcategorias]
    return data.set_index('categoria').T.to_dict()
