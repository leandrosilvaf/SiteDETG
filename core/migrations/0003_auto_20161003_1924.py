# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 22:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160921_1934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professor',
            old_name='area_de_conhecimento',
            new_name='linha_de_pesquisa',
        ),
    ]
