# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20160120_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='environment',
            name='record_date',
            field=models.DateTimeField(default=None),
        ),
    ]
