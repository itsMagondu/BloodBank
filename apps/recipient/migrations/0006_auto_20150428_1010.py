# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('recipient', '0005_auto_20150428_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 28, 10, 10, 7, 469529)),
            preserve_default=True,
        ),
    ]
