# Generated by Django 2.2.1 on 2019-09-05 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='password',
            name='email',
            field=models.EmailField(default='kan@kan.com', max_length=128),
            preserve_default=False,
        ),
    ]
