# Generated by Django 4.2.3 on 2023-10-23 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bat_app', '0050_alter_signal_entry_price_alter_signal_stoploss_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='signal',
            name='analysis',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]