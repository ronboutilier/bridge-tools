# Generated by Django 3.0.3 on 2020-08-23 18:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200821_0823'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.CharField(max_length=200)),
                ('audio_track', models.FileField(upload_to='getting_started/')),
            ],
        ),
        migrations.AlterField(
            model_name='element',
            name='element_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 23, 11, 25, 3, 86757), verbose_name='date published'),
        ),
    ]