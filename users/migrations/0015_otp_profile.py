# Generated by Django 3.0.9 on 2021-01-22 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.upload
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_mainuser_received_three_days_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='First name')),
                ('specialization', models.CharField(max_length=100, verbose_name='Specialization')),
                ('instagram_username', models.CharField(max_length=100, verbose_name='Instagram username')),
                ('avatar', models.FileField(upload_to=utils.upload.avatar_document_path, validators=[utils.validators.validate_file_size, utils.validators.basic_validate_images], verbose_name='Image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('code', models.CharField(max_length=4, verbose_name='Code')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='otps', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]