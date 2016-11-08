# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 23:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bolsista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projeto', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nome', models.CharField(max_length=20)),
                ('grau', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplinas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.DateField()),
                ('ementa', models.TextField(max_length=500)),
                ('arquivo', models.FileField(upload_to='core/arquivos')),
                ('codigo', models.ManyToManyField(to='core.Disciplina', verbose_name='lista de disciplinas')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=200)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='core')),
                ('nome', models.CharField(max_length=70)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('telefone', models.IntegerField()),
                ('horario_de_atendimento', models.DateTimeField()),
                ('cargo', models.CharField(max_length=70)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pesquisador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projeto', models.CharField(max_length=70)),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regime_de_trabalho', models.CharField(max_length=12)),
                ('lattes', models.CharField(max_length=70)),
                ('formacao', models.CharField(max_length=70)),
                ('area_de_conhecimento', models.TextField()),
                ('resumo', models.TextField()),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Publicacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField()),
                ('ano', models.DateField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico_adm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Funcionario')),
            ],
        ),
        migrations.AddField(
            model_name='professor',
            name='publicacoes',
            field=models.ManyToManyField(to='core.Publicacao', verbose_name='lista de publicacoes'),
        ),
        migrations.AddField(
            model_name='bolsista',
            name='matricula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Funcionario'),
        ),
        migrations.AddField(
            model_name='bolsista',
            name='orientador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Professor'),
        ),
    ]