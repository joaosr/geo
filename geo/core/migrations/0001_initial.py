# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-09 00:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Indice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indice', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('categoria', models.CharField(blank=True, max_length=100, null=True, verbose_name='Categoria')),
                ('subcategoria', models.CharField(blank=True, max_length=100, null=True, verbose_name='Subcategoria')),
                ('publicacao', models.DateField(blank=True, null=True, verbose_name='Publicado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('geocode', models.CharField(max_length=7)),
                ('state', models.CharField(max_length=2, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='indice',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Municipio'),
        ),
    ]
