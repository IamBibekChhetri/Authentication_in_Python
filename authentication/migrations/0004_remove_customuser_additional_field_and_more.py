# Generated by Django 4.2.2 on 2023-06-14 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remove_customuser_image_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='additional_field',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='phone',
        ),
    ]
