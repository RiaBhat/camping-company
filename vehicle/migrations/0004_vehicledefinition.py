# Generated by Django 2.0.7 on 2019-02-18 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_auto_20180917_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=64)),
                ('seat', models.CharField(max_length=12)),
                ('year', models.CharField(max_length=4)),
                ('available', models.BooleanField()),
                ('check_in_date', models.DateField(blank=True, null=True)),
                ('check_out_date', models.DateField(blank=True, null=True)),
                ('color', models.CharField(max_length=12)),
            ],
        ),
    ]