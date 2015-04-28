# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('recipient', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 4, 28, 7, 25, 14, 835548))),
                ('hospital', models.TextField()),
                ('bloodGroup', models.ForeignKey(to='recipient.BloodGroup')),
                ('location', models.ForeignKey(to='recipient.Locality')),
                ('user', models.ForeignKey(to='recipient.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('eta', models.TextField()),
                ('user', models.ForeignKey(to='recipient.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
