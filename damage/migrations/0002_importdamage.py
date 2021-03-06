# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-19 12:35
from __future__ import unicode_literals

import csv
from django.db import migrations

def ImportDamage(apps, schema_editor):
    Damage = apps.get_model('damage', 'Damage')
    Element = apps.get_model('elements', 'Element')
    with open('veekun/pokedex/data/csv/type_efficacy.csv', 'r') as efficacy_f:
        data = csv.DictReader(efficacy_f.read().splitlines())
    for row in data:
        Damage.objects.create(
            damage=Element.objects.get(pk=row['damage_type_id']),
            target=Element.objects.get(pk=row['target_type_id']),
            factor=row['damage_factor'],
        )

class Migration(migrations.Migration):

    dependencies = [
        ('damage', '0001_initial'),
        ('elements', '0002_importelements'),
    ]

    operations = [
        migrations.RunPython(ImportDamage),
    ]
