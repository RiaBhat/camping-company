# Generated by Django 2.0.7 on 2019-01-25 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20181126_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=256),
        ),
    ]
