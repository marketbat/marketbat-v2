# Generated by Django 4.2.3 on 2023-10-20 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bat_app', '0042_conversation_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]