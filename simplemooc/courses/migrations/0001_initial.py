# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Data de Início')),
                ('image', models.ImageField(upload_to='courses/images', verbose_name='Imagem')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
        ),
    ]
