# Generated by Django 3.0.9 on 2020-09-02 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0018_auto_20200820_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sphere_name', models.CharField(max_length=100, verbose_name='Sphere')),
                ('number', models.IntegerField(verbose_name='Number of goals')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User results',
            },
        ),
    ]