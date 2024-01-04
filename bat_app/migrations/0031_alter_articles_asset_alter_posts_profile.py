# Generated by Django 4.2.3 on 2023-09-26 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bat_app', '0030_alter_posts_post_polarity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='bat_app.assets'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='bat_app.profile'),
        ),
    ]