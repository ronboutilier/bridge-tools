# Generated by Django 3.0.3 on 2021-01-09 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210109_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='bridge_status',
            field=models.CharField(default=0, max_length=1),
        ),
    ]
