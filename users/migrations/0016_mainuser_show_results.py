# Generated by Django 3.0.9 on 2021-01-23 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_otp_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainuser',
            name='show_results',
            field=models.BooleanField(default=False, verbose_name='Show results'),
        ),
    ]