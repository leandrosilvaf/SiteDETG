# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-18 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_funcionario_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='slug',
            field=models.SlugField(null=True, verbose_name='Atalho'),
        ),
        migrations.AddField(
            model_name='publicacao',
            name='slug',
            field=models.SlugField(null=True, verbose_name='Atalho'),
        ),
    ]
