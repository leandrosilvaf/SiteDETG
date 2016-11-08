# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-24 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_tecnico_adm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
                ('slug', models.SlugField(max_length=70)),
                ('link', models.CharField(blank=True, max_length=50, null=True)),
                ('arquivo', models.FileField(blank=True, null=True, upload_to='core/documentos')),
            ],
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
                ('slug', models.SlugField(max_length=70)),
                ('link', models.CharField(blank=True, max_length=50, null=True)),
                ('arquivo', models.FileField(blank=True, null=True, upload_to='core/documentos')),
            ],
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
                ('slug', models.SlugField(max_length=70)),
                ('descricao', models.TextField()),
                ('link', models.CharField(blank=True, max_length=50, null=True)),
                ('arquivo', models.FileField(blank=True, null=True, upload_to='core/documentos')),
            ],
        ),
        migrations.CreateModel(
            name='Legislacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
                ('slug', models.SlugField(max_length=70)),
                ('link', models.CharField(blank=True, max_length=50, null=True)),
                ('arquivo', models.FileField(blank=True, null=True, upload_to='core/documentos')),
            ],
        ),
        migrations.DeleteModel(
            name='Documentos',
        ),
        migrations.AlterModelOptions(
            name='disciplina',
            options={'ordering': ['slug']},
        ),
        migrations.AlterModelOptions(
            name='professor',
            options={'ordering': ['slug']},
        ),
        migrations.AlterField(
            model_name='bolsista',
            name='slug',
            field=models.SlugField(max_length=70),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='nome',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='slug',
            field=models.SlugField(max_length=70),
        ),
        migrations.AlterField(
            model_name='pesquisador',
            name='slug',
            field=models.SlugField(max_length=70),
        ),
        migrations.AlterField(
            model_name='professor',
            name='slug',
            field=models.SlugField(max_length=70),
        ),
        migrations.AlterField(
            model_name='tecnico_adm',
            name='slug',
            field=models.SlugField(max_length=70),
        ),
    ]