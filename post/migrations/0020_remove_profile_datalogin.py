# Generated by Django 4.0.6 on 2022-07-21 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0019_profile_datalogin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='datalogin',
        ),
    ]