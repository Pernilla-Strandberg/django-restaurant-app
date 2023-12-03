# Generated by Django 4.2.7 on 2023-12-02 21:56

from django.db import migrations, models
import restaurant.models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_alter_bookingmodel_options_alter_bookingmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingmodel',
            name='email',
            field=models.EmailField(max_length=254, validators=[restaurant.models.validate_email]),
        ),
        migrations.AlterField(
            model_name='bookingmodel',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='bookingmodel',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]