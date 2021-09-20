# Generated by Django 3.0.9 on 2021-09-20 07:35

from django.db import migrations, models
import utils.upload
import utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=100, verbose_name='Name')),
                ('image', models.ImageField(upload_to=utils.upload.celebrity_avatar_document_path, validators=[utils.validators.validate_file_size, utils.validators.basic_validate_images], verbose_name='Image')),
                ('my_order', models.PositiveIntegerField(default=0, verbose_name='Order')),
            ],
            options={
                'ordering': ['my_order'],
            },
        ),
    ]
