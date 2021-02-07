# Generated by Django 3.0.3 on 2020-08-21 15:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200820_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='books/covers/'),
        ),
        migrations.AlterField(
            model_name='element',
            name='element_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 21, 8, 23, 53, 615517), verbose_name='date published'),
        ),
    ]
