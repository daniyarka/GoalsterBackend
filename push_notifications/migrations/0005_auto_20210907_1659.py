# Generated by Django 3.0.9 on 2021-09-07 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('push_notifications', '0004_disposablenotification_send_instantly'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disposablenotification',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date'),
        ),
    ]
