# Generated by Django 3.0.5 on 2020-10-06 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0004_auto_20201005_2302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='about',
            new_name='bio',
        ),
    ]
