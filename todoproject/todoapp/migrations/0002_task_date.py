# Generated by Django 3.2.15 on 2022-09-03 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateTimeField(default='2000-08-16'),
            preserve_default=False,
        ),
    ]
