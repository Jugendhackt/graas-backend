# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 09:30
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('count', models.IntegerField()),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
