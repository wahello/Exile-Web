# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novedades', '0004_auto_20170606_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporte',
            name='numero',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]