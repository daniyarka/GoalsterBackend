# Generated by Django 3.0.9 on 2021-01-24 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_mainuser_followers'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReactionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emoji', models.CharField(max_length=100, verbose_name='Emoji')),
            ],
            options={
                'verbose_name': 'Reaction type',
                'verbose_name_plural': 'Reaction types',
            },
        ),
        migrations.AlterField(
            model_name='mainuser',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='_mainuser_followers_+', to=settings.AUTH_USER_MODEL, verbose_name='Followers'),
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_reactions', to=settings.AUTH_USER_MODEL, verbose_name='Sender')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reactions', to='users.ReactionType', verbose_name='Type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_reactions', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Reaction',
                'verbose_name_plural': 'Reactions',
            },
        ),
    ]
