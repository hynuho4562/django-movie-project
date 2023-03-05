from django.db import models
import datetime

# Create your models here.
class User(models.Model):

    userName = models.CharField(max_length=20)
    userEmail = models.EmailField(max_length=100)
    hobby = models.CharField(max_length=50)
    favorite_movie = models.CharField(max_length=70)
    date = models.DateField(datetime.date.today())

    def __str__(self):
        return self.favorite_movie


class Movie(models.Model):
    movieName = models.ForeignKey(User, on_delete=models.CASCADE)
    currentView = models.IntegerField(default=0)
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.movieName
