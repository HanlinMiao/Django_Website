# Generated by Django 3.0.6 on 2020-06-22 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='author',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='date_posted',
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='photoGallery/'),
        ),
    ]
