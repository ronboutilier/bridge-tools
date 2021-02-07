# Generated by Django 3.0.3 on 2021-01-10 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210110_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='inspected',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='trip_notes',
        ),
        migrations.CreateModel(
            name='Trip_Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('structure_id', models.CharField(max_length=200)),
                ('trip_notes', models.CharField(max_length=200)),
                ('trip_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Selection_Sets', verbose_name='Set')),
            ],
            options={
                'verbose_name_plural': 'Trip_Notes',
            },
        ),
        migrations.CreateModel(
            name='Bridge_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('structure_id', models.CharField(max_length=200)),
                ('inspected', models.CharField(max_length=3)),
                ('trip_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Selection_Sets', verbose_name='Set')),
            ],
            options={
                'verbose_name_plural': 'Status',
            },
        ),
    ]