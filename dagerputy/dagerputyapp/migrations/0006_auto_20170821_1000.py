# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-21 10:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dagerputyapp', '0005_auto_20170818_1202'),
    ]

    operations = [
        migrations.DeleteModel(
            name='JenkinsStatusCheck',
        ),
        migrations.RenameModel(
            old_name='JenkinsCheck',
            new_name='JenkinsStatusCheck',
        )
    ]
