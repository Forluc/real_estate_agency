# Generated by Django 2.2.24 on 2023-07-16 12:56

from django.db import migrations


def add_flat_to_owner(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.owner_flats.add(flat.id)


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0013_auto_20230716_1506'),
    ]

    operations = [
        migrations.RunPython(add_flat_to_owner)
    ]
