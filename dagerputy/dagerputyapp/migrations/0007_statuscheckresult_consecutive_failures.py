# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-24 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dagerputyapp', '0006_auto_20170821_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='statuscheckresult',
            name='consecutive_failures',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
