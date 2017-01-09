# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(unique=True, max_length=30, verbose_name='Nome do Usuário')),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='E-mail')),
                ('name', models.CharField(verbose_name='Nome', max_length=100, blank=True)),
                ('is_active', models.BooleanField(verbose_name='Está ativo?', default=True)),
                ('is_staff', models.BooleanField(verbose_name='É da equipe?', default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Data de Entrada')),
                ('groups', models.ManyToManyField(related_name='user_set', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', related_query_name='user', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions', related_query_name='user', to='auth.Permission')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
