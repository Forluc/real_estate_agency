# Generated by Django 2.2.24 on 2023-07-13 17:42

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20230713_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, region=None, verbose_name='Нормализованный номер владельца'),
        ),
    ]