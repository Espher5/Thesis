# Generated by Django 3.0.6 on 2020-05-18 20:55

import UploadImage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UploadImage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='image',
            field=models.ImageField(upload_to=UploadImage.models.get_filename),
        ),
    ]
