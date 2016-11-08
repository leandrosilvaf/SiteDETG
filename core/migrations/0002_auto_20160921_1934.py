# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='area_de_conhecimento',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='lattes',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='publicacoes',
            field=models.ManyToManyField(blank=True, to='core.Publicacao', verbose_name='lista de publicacoes'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='resumo',
            field=models.TextField(blank=True, null=True),
        ),
    ]
