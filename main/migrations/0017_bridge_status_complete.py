# Generated by Django 3.0.3 on 2021-01-15 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20210110_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='bridge_status',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]