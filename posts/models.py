from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
       return self.name

class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.IntegerField(default=0)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name="movies")

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="review")
    stars = models.IntegerField(max_length=5, default=0)

    def __str__(self):
        return self.movie



