# Generated by Django 4.2.3 on 2023-11-30 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bat_app', '0067_remove_community_admin_remove_community_messages_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='list_date',
            field=models.DateField(default=''),
        ),
    ]
