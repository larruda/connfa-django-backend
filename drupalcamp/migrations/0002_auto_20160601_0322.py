# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-01 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drupalcamp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='iconURL',
            field=models.FileField(max_length=300, upload_to=b''),
        ),
    ]