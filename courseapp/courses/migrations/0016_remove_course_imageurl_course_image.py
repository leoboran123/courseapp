# Generated by Django 4.1.5 on 2023-02-11 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_uploadmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='imageUrl',
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
