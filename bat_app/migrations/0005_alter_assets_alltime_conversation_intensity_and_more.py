# Generated by Django 4.2.3 on 2023-07-11 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bat_app', '0004_alter_assets_alltime_conversation_intensity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='alltime_conversation_intensity',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='assets',
            name='month_conversation_intensity',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='assets',
            name='week_conversation_intensity',
            field=models.IntegerField(default=50),
        ),
    ]
