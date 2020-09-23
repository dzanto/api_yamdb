from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)

    def __str__(self):
        return self.slug


class Genres(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)

    def __str__(self):
        return self.slug


class Titles(models.Model):
    name = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    description = models.TextField()
    genre = models.ManyToManyField(Genres, verbose_name='Genres')
    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        related_name="titles", null=True
    )