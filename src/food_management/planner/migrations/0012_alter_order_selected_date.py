# Generated by Django 4.2.4 on 2023-08-22 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0011_alter_order_selected_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='selected_date',
            field=models.DateField(unique=True),
        ),
    ]
