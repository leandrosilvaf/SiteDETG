# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-19 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20161019_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='horario_de_atendimento',
            field=models.DateTimeField(),
        ),
    ]
