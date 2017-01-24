# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20170118_0117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('number', models.IntegerField(blank=True, verbose_name='Número (Ordem)', default=0)),
                ('release_date', models.DateTimeField(null=True, blank=True, verbose_name='Data de Liberação')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('course', models.ForeignKey(verbose_name='Curso', to='courses.Course', related_name='lessons')),
            ],
            options={
                'ordering': ['number'],
                'verbose_name_plural': 'Aulas',
                'verbose_name': 'Aula',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('embedded', models.TextField(blank=True, verbose_name='Vídeo embedded')),
                ('file', models.FileField(null=True, blank=True, upload_to='lessons/materials')),
                ('lesson', models.ForeignKey(verbose_name='aula', to='courses.Lesson', related_name='material')),
            ],
            options={
                'verbose_name_plural': 'Materiais',
                'verbose_name': 'Material',
            },
        ),
    ]
