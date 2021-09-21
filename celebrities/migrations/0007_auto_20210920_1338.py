# Generated by Django 3.0.9 on 2021-09-20 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celebrities', '0006_auto_20210920_1335'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='celebrity',
            options={'ordering': ['order'], 'verbose_name': 'Celebrity', 'verbose_name_plural': 'Celebrities'},
        ),
        migrations.RemoveField(
            model_name='celebrity',
            name='my_order',
        ),
        migrations.AlterField(
            model_name='celebrity',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Order'),
        ),
    ]