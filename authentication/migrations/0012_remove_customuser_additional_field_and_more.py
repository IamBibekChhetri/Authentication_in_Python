# Generated by Django 4.2.2 on 2023-06-15 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_alter_customuser_image_delete_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='additional_field',
        ),
        migrations.AddField(
            model_name='customuser',
            name='fullname',
            field=models.CharField(default='', max_length=100),
        ),
    ]
