# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20161004_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacao',
            name='arquivo',
            field=models.FileField(blank=True, null=True, upload_to='core/publicacao'),
        ),
    ]
