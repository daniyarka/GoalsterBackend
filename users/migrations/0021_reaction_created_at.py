# Generated by Django 3.0.9 on 2021-03-15 08:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20210312_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='reaction',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Creation date'),
            preserve_default=False,
        ),
    ]
