# Generated by Django 4.1.5 on 2023-03-08 14:45

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_remove_course_imageurl_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='subtitle',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
