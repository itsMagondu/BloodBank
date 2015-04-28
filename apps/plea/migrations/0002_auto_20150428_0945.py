# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('plea', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plea',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 28, 9, 45, 3, 458115)),
            preserve_default=True,
        ),
    ]
