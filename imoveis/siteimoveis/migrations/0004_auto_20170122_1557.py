# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteimoveis', '0003_auto_20170122_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='latitude',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='longitude',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
