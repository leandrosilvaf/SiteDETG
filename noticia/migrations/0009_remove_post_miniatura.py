# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 21:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0008_post_topico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='miniatura',
        ),
    ]
