# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import re
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('key', models.CharField(max_length=100, unique=True, verbose_name='Chave')),
                ('created_at', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('confirmed', models.BooleanField(default=False, verbose_name='Confirmado?')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'Nova Senha',
                'verbose_name_plural': 'Novas Senhas',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True, verbose_name='Nome do Usuário', validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'o nome do usuário só pode ter letras, digitos ou os seguintes caracteries: <./@/+/->', 'invalid')]),
        ),
        migrations.AddField(
            model_name='passwordreset',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]
