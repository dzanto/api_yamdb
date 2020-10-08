from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()


# CONTENT

class Categories(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ['-id']


class Genres(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ['-id']


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

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


# REVIEW

class Review(models.Model):
    text = models.TextField()
    score = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10, message="cool")])
    title = models.ForeignKey(Titles, blank=True, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_author")
    pub_date = models.DateTimeField("date published", auto_now_add=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    pub_date = models.DateTimeField("Дата добавления", auto_now_add=True, db_index=True)