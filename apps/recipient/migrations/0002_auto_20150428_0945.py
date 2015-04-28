# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('recipient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 28, 9, 45, 3, 460476)),
            preserve_default=True,
        ),
    ]
