# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-07 19:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0016_auto_20170907_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='fecha_ejecucion',
        ),
    ]