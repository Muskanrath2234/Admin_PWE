# Generated by Django 5.0.7 on 2024-08-22 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_Management', '0004_remove_profile_room_number_profile_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
