# Generated by Django 4.2.3 on 2023-07-11 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bat_app', '0009_remove_assets_market_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='assets',
            name='market_price',
            field=models.CharField(default='$1.0', max_length=100),
        ),
    ]