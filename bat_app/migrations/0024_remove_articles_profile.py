# Generated by Django 4.2.3 on 2023-09-26 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bat_app', '0023_articles_article_polarity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='profile',
        ),
    ]