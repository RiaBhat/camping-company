# Generated by Django 2.2.1 on 2019-07-13 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='night_time_temperature',
            field=models.CharField(max_length=64),
        ),
    ]