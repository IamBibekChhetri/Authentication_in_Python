# Generated by Django 4.2.2 on 2023-06-20 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_remove_customuser_image_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='otp',
            field=models.IntegerField(max_length=6, null=True),
        ),
    ]
