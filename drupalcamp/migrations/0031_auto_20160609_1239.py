# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-09 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drupalcamp', '0030_auto_20160608_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='webSite',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
