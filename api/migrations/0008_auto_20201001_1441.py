# Generated by Django 3.0.5 on 2020-10-01 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20201001_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='genres',
            name='slug',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]