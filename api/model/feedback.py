from django.contrib.auth import get_user_model
from django.db import models
from api.model.content import Titles
from django.core.validators import MaxValueValidator, MinValueValidator 

User = get_user_model()


class Review(models.Model):
    text = models.TextField()
    score = models .PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10, message="cool")])
    title = models.ForeignKey(Titles, blank=True, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_author")

    

    def __str__(self):
        return self.text

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created = models.DateTimeField("Дата добавления", auto_now_add=True, db_index=True)    