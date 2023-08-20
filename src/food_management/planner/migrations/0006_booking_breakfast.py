# Generated by Django 4.2.4 on 2023-08-20 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0005_remove_booking_breakfast'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='breakfast',
            field=models.CharField(choices=[('idli', 'Idli'), ('puttu', 'Puttu'), ('dosa', 'dosa'), ('appam', 'Appam')], default='food', max_length=200),
            preserve_default=False,
        ),
    ]