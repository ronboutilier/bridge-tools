# Generated by Django 3.0.3 on 2021-01-15 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_bridge_status_complete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bridge_status',
            name='inspected',
        ),
    ]
