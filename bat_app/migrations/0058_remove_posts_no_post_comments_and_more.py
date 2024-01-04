# Generated by Django 4.2.3 on 2023-10-25 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bat_app', '0057_remove_profile_interests_delete_interest_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='no_post_comments',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='no_post_likes',
        ),
        migrations.AddField(
            model_name='posts',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='profile_comments', to='bat_app.comments'),
        ),
        migrations.AddField(
            model_name='posts',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='profile_likes', to='bat_app.profile'),
        ),
        migrations.AddField(
            model_name='posts',
            name='post_video',
            field=models.FileField(blank=True, upload_to='post_videos'),
        ),
        migrations.AddField(
            model_name='posts',
            name='reposts',
            field=models.ManyToManyField(blank=True, related_name='profile_reposts', to='bat_app.profile'),
        ),
    ]