# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_lesson_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='lesson',
            field=models.ForeignKey(related_name='materials', to='courses.Lesson', verbose_name='aula'),
        ),
    ]
