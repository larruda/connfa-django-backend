# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-07 03:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drupalcamp', '0021_auto_20160607_0250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bof',
            name='type',
        ),
        migrations.AddField(
            model_name='bof',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drupalcamp.Type'),
        ),
        migrations.RemoveField(
            model_name='session',
            name='type',
        ),
        migrations.AddField(
            model_name='session',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drupalcamp.Type'),
        ),
        migrations.RemoveField(
            model_name='socialevent',
            name='type',
        ),
        migrations.AddField(
            model_name='socialevent',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drupalcamp.Type'),
        ),
    ]