# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20160120_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='environment',
            name='light',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='environment',
            name='soid_humidity',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='environment',
            name='soid_temperature',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
