# Generated by Django 4.2.7 on 2023-11-28 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_bookingmodel_options_bookingmodel_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingmodel',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bookingmodel',
            name='day',
            field=models.DateField(verbose_name='Visiting date'),
        ),
    ]