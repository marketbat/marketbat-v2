# Generated by Django 4.2.3 on 2023-07-10 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bat_app', '0002_assets_new_drop_assets_trending_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assets',
            name='yesterday_conversation_volume',
            field=models.IntegerField(default=0),
        ),
    ]