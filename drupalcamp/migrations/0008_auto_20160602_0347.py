# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-02 03:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drupalcamp', '0007_auto_20160602_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='order',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True),
        ),
    ]
