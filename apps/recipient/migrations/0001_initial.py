# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('rhesus', models.BooleanField(default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('center', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.TextField()),
                ('lastname', models.TextField(null=True)),
                ('othername', models.TextField(null=True)),
                ('gender', models.TextField(null=True)),
                ('DOB', models.TextField(null=True)),
                ('cellphone', models.TextField()),
                ('joined', models.DateTimeField(default=datetime.datetime(2015, 4, 28, 7, 25, 26, 938856))),
                ('bloodGroup', models.ForeignKey(to='recipient.BloodGroup')),
                ('location', models.ForeignKey(to='recipient.Locality')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserIllness',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disease', models.TextField()),
                ('user', models.ForeignKey(to='recipient.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
