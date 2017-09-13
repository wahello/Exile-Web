# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-07 19:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0015_auto_20170907_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multimedia',
            name='audio',
        ),
        migrations.RemoveField(
            model_name='multimedia',
            name='foto',
        ),
        migrations.AddField(
            model_name='multimedia',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='multimedia',
            name='tipo',
            field=models.IntegerField(choices=[(1, 'Foto'), (2, 'Multimedia')], default=1),
            preserve_default=False,
        ),
    ]