# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-05 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drupalcamp', '0015_auto_20160605_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('name', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('version', models.CharField(max_length=200)),
                ('link', models.URLField(blank=True, null=True)),
                ('order', models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True)),
                ('deleted', models.BooleanField()),
                ('experienceLevel', models.ManyToManyField(blank=True, to='drupalcamp.Level')),
                ('speakers', models.ManyToManyField(blank=True, to='drupalcamp.Speaker')),
                ('track', models.ManyToManyField(blank=True, to='drupalcamp.Track')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
