# Generated by Django 4.2.2 on 2023-06-16 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipparams', '0003_t1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t1',
            name='Price',
            field=models.FloatField(default=0),
        ),
    ]
