# Generated by Django 4.2.7 on 2023-12-01 14:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("restaurant", "0003_alter_bookingmodel_created_on_alter_bookingmodel_day"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bookingmodel",
            options={"ordering": ["day", "time"], "verbose_name": "Booking"},
        ),
        migrations.AlterField(
            model_name="bookingmodel",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_bookings",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
