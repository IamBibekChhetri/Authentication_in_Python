# Generated by Django 4.2.2 on 2023-06-15 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_customuser_additional_field_customuser_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='profileImage/'),
        ),
    ]
