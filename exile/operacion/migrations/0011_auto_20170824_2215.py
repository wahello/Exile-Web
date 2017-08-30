# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-24 22:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0010_auto_20170614_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multimedia',
            name='completado',
        ),
        migrations.AddField(
            model_name='multimedia',
            name='tarea',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='operacion.Tarea'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='completado',
            name='tarea',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='operacion.Tarea'),
        ),
        migrations.AlterField(
            model_name='completadosub',
            name='subtarea',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='operacion.SubTarea'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='empleados',
            field=models.ManyToManyField(blank=True, to='usuarios.Empleado'),
        ),
    ]
