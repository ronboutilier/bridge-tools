# Generated by Django 3.1.6 on 2021-02-12 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('steamroller', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='workout_date',
        ),
    ]
