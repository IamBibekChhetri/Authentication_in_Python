# Generated by Django 4.2.2 on 2023-06-15 03:54

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_customuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='additional_field',
            field=models.CharField(default=datetime.datetime(2023, 6, 15, 3, 54, 6, 271158, tzinfo=datetime.timezone.utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
