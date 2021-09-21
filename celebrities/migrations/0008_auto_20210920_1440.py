# Generated by Django 3.0.9 on 2021-09-20 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celebrities', '0007_auto_20210920_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='celebritygoal',
            name='name',
        ),
        migrations.RemoveField(
            model_name='celebrityprofile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='celebrityprofile',
            name='specialization',
        ),
        migrations.RemoveField(
            model_name='celebritysphere',
            name='name',
        ),
        migrations.AddField(
            model_name='celebritygoal',
            name='name_en',
            field=models.TextField(default='test', verbose_name='Название EN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='celebritygoal',
            name='name_ru',
            field=models.TextField(default='test', verbose_name='Название RU'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='celebrityprofile',
            name='name_en',
            field=models.CharField(default='test', max_length=100, verbose_name='Имя EN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='celebrityprofile',
            name='name_ru',
            field=models.CharField(default='test', max_length=100, verbose_name='Имя RU'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='celebrityprofile',
            name='specialization_en',
            field=models.CharField(default='test', max_length=100, verbose_name='Специализация EN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='celebrityprofile',
            name='specialization_ru',
            field=models.CharField(default='test', max_length=100, verbose_name='Специализация RU'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='celebritysphere',
            name='name_en',
            field=models.CharField(default='test', max_length=100, verbose_name='Название EN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='celebritysphere',
            name='name_ru',
            field=models.CharField(default='test', max_length=100, verbose_name='Название RU'),
            preserve_default=False,
        ),
    ]