# Generated by Django 4.2.2 on 2023-06-16 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipparams', '0002_remove_ship_params_distance_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='t1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Zones', models.IntegerField(default=100)),
                ('Weight', models.IntegerField(default=0)),
                ('Time', models.IntegerField(default=0)),
                ('Price', models.IntegerField(default=0)),
            ],
        ),
    ]