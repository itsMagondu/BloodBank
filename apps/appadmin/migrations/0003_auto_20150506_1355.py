# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0002_auto_20150506_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteemail',
            name='message',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='websiteemail',
            name='sender',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
