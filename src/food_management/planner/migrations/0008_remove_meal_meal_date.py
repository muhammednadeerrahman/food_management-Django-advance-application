# Generated by Django 4.2.4 on 2023-08-21 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0007_delete_booking_meal_is_draft_meal_meal_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='meal_date',
        ),
    ]
