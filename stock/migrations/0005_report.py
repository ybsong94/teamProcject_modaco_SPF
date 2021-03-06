# Generated by Django 3.2.5 on 2021-07-22 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_rename_kospi_date_kosdaq_kosdaq_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_stock', models.CharField(max_length=30)),
                ('report_title', models.CharField(max_length=200)),
                ('report_publisher', models.CharField(max_length=30)),
                ('report_date', models.CharField(max_length=50)),
                ('report_link', models.URLField()),
            ],
        ),
    ]
