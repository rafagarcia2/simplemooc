# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='threads',
            field=models.ForeignKey(related_name='replies', verbose_name='Tópico', to='forum.Thread'),
            preserve_default=False,
        ),
    ]
