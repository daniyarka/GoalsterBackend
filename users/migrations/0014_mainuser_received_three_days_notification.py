# Generated by Django 3.0.9 on 2020-10-04 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_delete_useractivation'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainuser',
            name='received_three_days_notification',
            field=models.BooleanField(blank=True, default=False, verbose_name='Received notification after 3 inactive days'),
        ),
    ]