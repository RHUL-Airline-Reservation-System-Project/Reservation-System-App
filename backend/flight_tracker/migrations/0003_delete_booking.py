# Generated by Django 5.2 on 2025-05-13 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("flight_tracker", "0002_booking"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Booking",
        ),
    ]
