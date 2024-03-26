from django.db import models

# Create your models here.

class Genre(models.Model) :
    name = models.CharField(max_len=255);

class Movies(models.Model) :
    title = models.CharField(max_len = 255);
    release_year = models.IntegerField();
    number_in_stock = models.IntegerField();
    daily_rate = models.FloatField();
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
