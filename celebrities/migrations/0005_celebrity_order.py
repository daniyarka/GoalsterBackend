# Generated by Django 3.0.9 on 2021-09-17 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celebrities', '0004_celebritygoal_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='celebrity',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Order'),
        ),
    ]