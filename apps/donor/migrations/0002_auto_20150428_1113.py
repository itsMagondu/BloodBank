# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='active',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bloodgroup',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='county',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
