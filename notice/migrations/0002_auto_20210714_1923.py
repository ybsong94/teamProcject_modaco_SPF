# Generated by Django 3.2.5 on 2021-07-14 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='file_upload',
            field=models.FileField(blank=True, upload_to='notice/files/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='head_image',
            field=models.ImageField(blank=True, upload_to='notice/images/%Y/%m/%d/'),
        ),
    ]