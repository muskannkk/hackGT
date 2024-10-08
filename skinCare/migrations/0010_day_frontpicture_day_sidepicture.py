# Generated by Django 5.1.1 on 2024-09-29 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skinCare', '0009_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='frontPicture',
            field=models.ImageField(blank=True, null=True, upload_to='front_pictures'),
        ),
        migrations.AddField(
            model_name='day',
            name='sidePicture',
            field=models.ImageField(blank=True, null=True, upload_to='side_pictures'),
        ),
    ]
