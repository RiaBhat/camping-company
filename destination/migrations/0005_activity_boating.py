# Generated by Django 2.2.1 on 2019-07-13 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0004_auto_20190713_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='boating',
            field=models.CharField(default='No', max_length=64),
        ),
    ]
