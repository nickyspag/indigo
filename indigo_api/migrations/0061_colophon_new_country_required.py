# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-21 18:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indigo_api', '0060_colophon_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colophon',
            name='new_country',
            field=models.ForeignKey(help_text=b'Which country does this colophon apply to?', on_delete=django.db.models.deletion.CASCADE, to='indigo_api.Country'),
        ),
    ]
