# Generated by Django 3.0.3 on 2021-01-10 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210110_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='trip_notes',
            field=models.CharField(max_length=200),
        ),
    ]
