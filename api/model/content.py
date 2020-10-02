from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


User = get_user_model()


class Categories(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.slug


class Genres(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.slug


class Titles(models.Model):
    name = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    description = models.TextField()
    genre = models.ManyToManyField(Genres)
    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        related_name="titles", null=True
    )
    rating = models.IntegerField(null=True)

    def __str__(self):
        return self.name

   
