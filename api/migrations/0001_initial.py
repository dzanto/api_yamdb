# Generated by Django 3.0.5 on 2020-10-09 06:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('category', models.ForeignKey(null=True,
                                               on_delete=django.db.models.deletion.SET_NULL,
                                               related_name='titles',
                                               to='api.Categories')),
                ('genre', models.ManyToManyField(to='api.Genres')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('score', models.PositiveIntegerField(
                    validators=[django.core.validators.MinValueValidator(0),
                                django.core.validators.MaxValueValidator(10,
                                                                         message='cool')])),
                ('pub_date', models.DateTimeField(auto_now_add=True,
                                                  verbose_name='date published')),
                ('author',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='review_author',
                                   to=settings.AUTH_USER_MODEL)),
                ('title', models.ForeignKey(blank=True,
                                            on_delete=django.db.models.deletion.CASCADE,
                                            related_name='reviews',
                                            to='api.Titles')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('pub_date',
                 models.DateTimeField(auto_now_add=True, db_index=True,
                                      verbose_name='Дата добавления')),
                ('author',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='comments',
                                   to=settings.AUTH_USER_MODEL)),
                ('review',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='comments', to='api.Review')),
            ],
        ),
    ]
