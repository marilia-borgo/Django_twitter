# Generated by Django 4.0.6 on 2022-07-21 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]