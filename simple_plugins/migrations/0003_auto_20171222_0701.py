# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-22 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_plugins', '0002_auto_20171208_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simplepageteaserpluginmodel',
            name='flavor',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='simpletextpluginmodel',
            name='flavor',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='simpletextpluginmodel',
            name='title',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='textandimagepluginmodel',
            name='flavor',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='textandimagepluginmodel',
            name='title',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
