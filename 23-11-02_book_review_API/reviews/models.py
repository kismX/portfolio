from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} by {self.author}"


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1, message="Der Wert muss mindestens 1 sein!"),
            MaxValueValidator(5, message="Der Wert darf höchstens 5 sein!")
        ]
    )

    def __str__(self):
        return f"Review of {self.book}"