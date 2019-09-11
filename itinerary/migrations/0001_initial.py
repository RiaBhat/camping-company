# Generated by Django 2.2.1 on 2019-07-13 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('destination', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.TimeField(auto_now_add=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('destination', models.ManyToManyField(blank=True, related_name='trips', to='destination.Destination')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itinerary_check', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
