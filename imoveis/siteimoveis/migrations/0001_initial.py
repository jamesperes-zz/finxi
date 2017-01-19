# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 01:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=100)),
                ('imagem', models.ImageField(upload_to='uploads/')),
                ('valor', models.FloatField()),
                ('bairro', models.CharField(max_length=100)),
                ('anuncio', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=11)),
            ],
        ),
        migrations.AddField(
            model_name='imovel',
            name='vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteimoveis.Vendedor'),
        ),
    ]
