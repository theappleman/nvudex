# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-19 10:28
from __future__ import unicode_literals

import csv
from django.db import migrations

def ImportElements(apps, schema_editor):
    Element = apps.get_model("elements", "Element")
    with open("veekun/pokedex/data/csv/types.csv", 'r') as type_f:
        data = csv.DictReader(type_f.read().splitlines())
    for row in data:
        Element.objects.create(
            id=row['id'],
            identifier=row['identifier'],
        )

class Migration(migrations.Migration):

    dependencies = [
        ('elements', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(ImportElements),
    ]