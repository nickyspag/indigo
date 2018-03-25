# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-14 15:31
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations
from cobalt.act import Act, datestring


def set_amendment_details(apps, schema_editor):
    Document = apps.get_model("indigo_api", "Document")
    db_alias = schema_editor.connection.alias
    for doc in Document.objects.using(db_alias).all():
        a = Act(doc.document_xml)
        amendments = a.amendments
        if amendments:
            doc.amendment_events = [{
                'date': datestring(e.date),
                'amending_title': e.amending_title,
                'amending_uri': e.amending_uri,
            } for e in amendments]
            doc.save()


class Migration(migrations.Migration):

    dependencies = [
        ('indigo_api', '0034_repeal'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='amendment_events',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.RunPython(
            set_amendment_details,
            migrations.RunPython.noop,)
    ]