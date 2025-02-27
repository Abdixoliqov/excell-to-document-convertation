# Generated by Django 5.0.7 on 2024-07-18 05:27

import app.models
import app.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='excel_file',
            field=models.FileField(upload_to=app.utils.file_path, validators=[app.models.validate_excel]),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
