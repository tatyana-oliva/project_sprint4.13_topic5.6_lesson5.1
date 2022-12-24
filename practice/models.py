from django.db import models

# Create your models here.
GENRE_CHOICES = (
    ("R", "Рок"),
    ("E", "Электроника"),
    ("P", "Поп"),
    ("C", "Классика"),
    ("O", "Саундтреки"),
)


class CD(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    artist = models.CharField(max_length=40)
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)

    def __repr__(self):
        return "Вот я такой кросавчик"


class ExchangeModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=40)
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES, default='R')
    price = models.DecimalField(decimal_places=2, max_digits=6)
    comment = models.CharField(max_length=1024)