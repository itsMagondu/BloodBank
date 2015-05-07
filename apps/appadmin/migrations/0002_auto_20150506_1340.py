# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='websiteemail',
            old_name='recieved',
            new_name='received',
        ),
        migrations.AlterField(
            model_name='websiteemail',
            name='email',
            field=models.EmailField(default=b'', max_length=75),
            preserve_default=True,
        ),
    ]
