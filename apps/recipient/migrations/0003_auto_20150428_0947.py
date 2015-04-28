# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('recipient', '0002_auto_20150428_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 28, 9, 47, 1, 122069)),
            preserve_default=True,
        ),
    ]
