# Generated by Django 2.2.1 on 2019-06-27 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Definition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(blank=True, max_length=64, null=True)),
                ('seat', models.CharField(blank=True, max_length=12, null=True)),
                ('year', models.CharField(blank=True, max_length=4, null=True)),
                ('available', models.BooleanField(default=False)),
                ('check_in_date', models.DateField(blank=True, null=True)),
                ('check_out_date', models.DateField(blank=True, null=True)),
                ('color', models.CharField(blank=True, max_length=12, null=True)),
                ('car_image', models.ImageField(blank=True, null=True, upload_to='cars')),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VehicleCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine_oil_level', models.PositiveIntegerField()),
                ('brake_fluid_level', models.PositiveIntegerField()),
                ('water_level', models.PositiveIntegerField()),
                ('windscreen_washer', models.BooleanField()),
                ('seatbelts_check', models.BooleanField()),
                ('parking_brake', models.BooleanField()),
                ('clutch_gearshift', models.BooleanField()),
                ('burning_smell', models.BooleanField()),
                ('steering_alignment', models.BooleanField()),
                ('dashboard', models.BooleanField()),
                ('check_lights', models.BooleanField()),
                ('horn', models.BooleanField()),
                ('tyres', models.BooleanField()),
                ('leakage', models.BooleanField()),
                ('active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_check', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]