# Generated by Django 2.1 on 2018-10-05 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world_challenge_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
