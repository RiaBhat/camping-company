# Generated by Django 2.2.1 on 2019-10-05 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0019_auto_20191005_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='amount',
            field=models.FloatField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='txnid',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]