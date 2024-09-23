# Generated by Django 4.0.3 on 2022-04-27 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armsApp', '0004_remove_flights_slots_flights_business_class_price_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flights',
            options={'verbose_name_plural': 'List of Flights'},
        ),
        migrations.RenameField(
            model_name='flights',
            old_name='economy_class_price',
            new_name='economy_price',
        ),
        migrations.RenameField(
            model_name='flights',
            old_name='economy_class_slots',
            new_name='economy_slots',
        ),
    ]
