# Generated by Django 4.1 on 2022-09-03 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_location_address_location_lat_location_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='long',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]