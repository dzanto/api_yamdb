# Generated by Django 3.0.5 on 2020-10-02 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20201001_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='titles',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]