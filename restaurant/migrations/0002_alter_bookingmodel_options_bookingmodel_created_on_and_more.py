# Generated by Django 4.2.7 on 2023-11-28 11:17

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bookingmodel",
            options={"ordering": ["day", "time"]},
        ),
        migrations.AddField(
            model_name="bookingmodel",
            name="created_on",
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="bookingmodel",
            name="email",
            field=models.EmailField(default="example@example.com", max_length=254),
        ),
        migrations.AddField(
            model_name="bookingmodel",
            name="first_name",
            field=models.CharField(default="First name", max_length=50),
        ),
        migrations.AddField(
            model_name="bookingmodel",
            name="last_name",
            field=models.CharField(default="Last name", max_length=50),
        ),
        migrations.AddField(
            model_name="bookingmodel",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="bookingmodel",
            name="day",
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="bookingmodel",
            name="guests",
            field=models.CharField(
                choices=[
                    ("1", "1"),
                    ("2", "2"),
                    ("3", "3"),
                    ("4", "4"),
                    ("5", "5"),
                    ("6", "6"),
                    ("7", "7"),
                    ("8", "8"),
                    ("9", "9"),
                    ("10", "10"),
                    ("10+C", "10+ - Contact Me"),
                ],
                default="2",
                help_text="Select number of guests",
                max_length=4,
            ),
        ),
        migrations.AlterField(
            model_name="bookingmodel",
            name="time",
            field=models.CharField(
                choices=[
                    ("6 PM", "6 PM"),
                    ("7 PM", "7 PM"),
                    ("8 PM", "8 PM"),
                    ("9 PM", "9 PM"),
                    ("10 PM", "10 PM"),
                ],
                default="6 PM",
                max_length=10,
            ),
        ),
    ]
