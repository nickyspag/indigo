# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-21 18:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indigo_api', '0061_colophon_new_country_required'),
    ]

    operations = [
        migrations.RemoveField('Colophon', 'country'),
        migrations.RenameField('Colophon', 'new_country', 'country'),
    ]
