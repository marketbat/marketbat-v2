# Generated by Django 4.2.3 on 2023-09-26 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bat_app', '0025_posts_post_polarity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='market_price',
            field=models.IntegerField(default=0),
        ),
    ]