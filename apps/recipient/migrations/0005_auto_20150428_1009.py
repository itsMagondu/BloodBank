# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('recipient', '0004_auto_20150428_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 28, 10, 9, 44, 999769)),
            preserve_default=True,
        ),
    ]
