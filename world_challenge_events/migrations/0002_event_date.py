# Generated by Django 2.1 on 2018-08-30 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world_challenge_events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]