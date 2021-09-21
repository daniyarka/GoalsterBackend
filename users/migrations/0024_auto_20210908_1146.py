# Generated by Django 3.0.9 on 2021-09-08 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_auto_20210908_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainuser',
            name='topic',
            field=models.CharField(blank=True, choices=[('1', 'RU'), ('2', 'EN')], max_length=10, null=True, verbose_name='Firebase topic'),
        ),
    ]