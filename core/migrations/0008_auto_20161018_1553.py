# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-18 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20161018_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacao',
            name='slug',
        ),
        migrations.AddField(
            model_name='documentos',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='slug',
            field=models.SlugField(),
        ),
    ]