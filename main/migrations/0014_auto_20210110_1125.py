# Generated by Django 3.0.3 on 2021-01-10 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210110_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='inspected',
            field=models.CharField(max_length=3),
        ),
    ]
