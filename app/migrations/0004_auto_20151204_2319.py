# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-05 05:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20151204_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='guia',
            name='Guiahtml',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='guia',
            name='Descripcion_guia',
            field=models.CharField(max_length=120),
        ),
    ]
