# Generated by Django 5.0.6 on 2025-03-26 09:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Listings', '0003_remove_propertylisting_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='event',
            name='time_from',
            field=models.TimeField(default=datetime.time(11, 30, 14, 999844)),
        ),
        migrations.AddField(
            model_name='event',
            name='time_to',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]
