# Generated by Django 4.0.6 on 2022-07-21 17:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0018_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='datalogin',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
