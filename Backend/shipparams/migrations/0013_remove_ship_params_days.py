# Generated by Django 4.2.2 on 2023-07-17 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipparams', '0012_t2_remove_ship_params_lat1_remove_ship_params_lat2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ship_params',
            name='days',
        ),
    ]
