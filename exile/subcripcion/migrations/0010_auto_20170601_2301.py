# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subcripcion', '0009_auto_20170601_0627'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plan',
            options={'verbose_name': 'Plan', 'verbose_name_plural': 'Planes'},
        ),
        migrations.AlterField(
            model_name='funcionalidad',
            name='url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
