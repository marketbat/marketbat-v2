# Generated by Django 4.2.3 on 2023-10-24 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bat_app', '0053_community_conversation_category_communitymessage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='cover_image',
            field=models.FileField(blank=True, null=True, upload_to='community_cover'),
        ),
        migrations.AddField(
            model_name='community',
            name='display_image',
            field=models.FileField(blank=True, null=True, upload_to='community_dp'),
        ),
    ]