# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-20 23:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novedades', '0008_remove_reporte_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotoreporte',
            name='foto',
            field=models.FileField(default=1, upload_to='fotos'),
            preserve_default=False,
        ),
    ]