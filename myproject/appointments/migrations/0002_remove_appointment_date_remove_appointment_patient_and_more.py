# Generated by Django 4.2.13 on 2024-07-09 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='speciality',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
