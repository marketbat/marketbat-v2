# Generated by Django 4.2.3 on 2023-12-29 09:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bat_app', '0070_remove_articles_article_keywords_interests_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('display_image', models.FileField(blank=True, null=True, upload_to='community_dp')),
                ('cover_image', models.FileField(blank=True, null=True, upload_to='community_cover')),
                ('date_started', models.DateTimeField(default=datetime.datetime.now)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bat_app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Inbox', 'Inbox'), ('Request', 'Request')], default='Request', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_sentiment',
            field=models.CharField(choices=[('Bullish', 'Bullish'), ('Bearish', 'Bearish'), ('Neutral', 'Neutral')], default='Neutral', max_length=100),
        ),
        migrations.CreateModel(
            name='Signal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chart', models.FileField(blank=True, null=True, upload_to='signal_charts')),
                ('order_type', models.CharField(choices=[('Buy', 'Buy'), ('Sell', 'Sell'), ('Buy Stop', 'Buy Stop'), ('Sell Stop', 'Sell Stop'), ('Buy Limit', 'Buy Limit'), ('Sell Limit', 'Sell Limit')], max_length=100)),
                ('analysis', models.TextField(blank=True)),
                ('entry_price', models.CharField(max_length=100)),
                ('takeprofit', models.CharField(max_length=100)),
                ('stoploss', models.CharField(max_length=100)),
                ('expiry', models.DateTimeField()),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bat_app.assets')),
                ('downvotes', models.ManyToManyField(blank=True, related_name='profile_downvotes', to='bat_app.profile')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_signal', to='bat_app.profile')),
                ('upvotes', models.ManyToManyField(blank=True, related_name='profile_upvotes', to='bat_app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(choices=[('Text', 'Text'), ('Image', 'Image'), ('Video', 'Video')], default='Text', max_length=10)),
                ('text', models.TextField()),
                ('media_file', models.FileField(blank=True, null=True, upload_to='message_media')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bat_app.conversation')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bat_app.profile')),
            ],
        ),
        migrations.AddField(
            model_name='conversation',
            name='messages',
            field=models.ManyToManyField(related_name='messages', to='bat_app.message'),
        ),
        migrations.AddField(
            model_name='conversation',
            name='participants',
            field=models.ManyToManyField(related_name='conversations', to='bat_app.profile'),
        ),
        migrations.CreateModel(
            name='CommunityMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(choices=[('Text', 'Text'), ('Image', 'Image'), ('Video', 'Video')], default='Text', max_length=10)),
                ('text', models.TextField()),
                ('media_file', models.FileField(blank=True, null=True, upload_to='message_media')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bat_app.community')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bat_app.profile')),
            ],
        ),
        migrations.AddField(
            model_name='community',
            name='messages',
            field=models.ManyToManyField(blank=True, related_name='group_messages', to='bat_app.communitymessage'),
        ),
        migrations.AddField(
            model_name='community',
            name='participants',
            field=models.ManyToManyField(related_name='group_conversations', to='bat_app.profile'),
        ),
    ]