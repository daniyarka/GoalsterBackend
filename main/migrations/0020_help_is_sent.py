# Generated by Django 3.0.9 on 2020-10-24 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_userresults'),
    ]

    operations = [
        migrations.AddField(
            model_name='help',
            name='is_sent',
            field=models.BooleanField(blank=True, default=False, verbose_name='Sent'),
        ),
    ]