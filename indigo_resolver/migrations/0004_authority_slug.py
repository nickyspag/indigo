# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-02 17:55
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('indigo_resolver', '0003_auto_20170506_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='authority',
            name='slug',
            field=models.CharField(null=True, unique=True, max_length=50, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_.]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores, dots or hyphens.", 'invalid')]),
        ),
    ]
