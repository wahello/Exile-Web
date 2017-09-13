# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-07 23:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0017_remove_tarea_fecha_ejecucion'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='fecha_ejecucion',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='multimedia',
            name='tipo',
            field=models.IntegerField(choices=[(1, 'Foto'), (2, 'Audio')]),
        ),
    ]