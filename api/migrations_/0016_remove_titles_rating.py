# Generated by Django 3.0.5 on 2020-10-05 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_merge_20201005_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='titles',
            name='rating',
        ),
    ]