# Generated by Django 4.2.3 on 2023-09-13 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bat_app', '0015_remove_profile_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='display_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
