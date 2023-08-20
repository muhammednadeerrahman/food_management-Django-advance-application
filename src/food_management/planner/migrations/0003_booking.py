# Generated by Django 4.2.4 on 2023-08-20 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_remove_meal_meal_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breakfast', models.CharField(choices=[('idli', 'Idli'), ('puttu', 'Puttu'), ('dosa', 'dosa'), ('appam', 'Appam')], max_length=200)),
                ('lunch', models.CharField(choices=[('chicken biriyani', 'Chicken Biriyani'), ('meals', 'Meals'), ('fried rice', 'Fried Rice'), ('ghee rice and curry', 'Ghee Rice and Curry')], max_length=200)),
                ('snack', models.CharField(choices=[('chicken biriyani', 'Chicken Biriyani'), ('meals', 'Meals'), ('fried rice', 'Fried Rice'), ('ghee rice and curry', 'Ghee Rice and Curry')], max_length=200)),
                ('dinner', models.CharField(choices=[('porota/chappathi with Egg Curry', 'porota/chappathi with Egg Curry'), ('meals', 'Meals'), ('fried rice', 'Fried Rice'), ('ghee rice and curry', 'Ghee Rice and Curry')], max_length=200)),
                ('current_time', models.DateTimeField()),
                ('is_draft', models.BooleanField(default=False)),
            ],
        ),
    ]
