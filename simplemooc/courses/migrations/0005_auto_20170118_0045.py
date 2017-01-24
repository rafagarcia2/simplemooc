# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0004_auto_20170113_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('content', models.TextField(verbose_name='Conteúdo')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(verbose_name='Atualizado em', auto_now=True)),
                ('course', models.ForeignKey(to='courses.Course', verbose_name='Curso')),
            ],
            options={
                'verbose_name_plural': 'Anúncios',
                'ordering': ['-create_at'],
                'verbose_name': 'Anúncio',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Comentário')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(verbose_name='Atualizado em', auto_now=True)),
                ('announcement', models.ForeignKey(to='courses.Announcement', verbose_name='Anúncio', related_name='comments')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='usuário')),
            ],
            options={
                'verbose_name_plural': 'Comentários',
                'ordering': ['create_at'],
                'verbose_name': 'Comentário',
            },
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='status',
            field=models.IntegerField(default=1, choices=[(0, 'Pendente'), (1, 'Aprovado'), (2, 'Cancelado')], blank=True, verbose_name='Situação'),
        ),
    ]
