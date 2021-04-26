from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_img = models.TextField()

    def __str__(self):
        return self.username


class Studio(models.Model):
    studio_name = models.CharField(max_length=64)

    def __str__(self):
        return self.studio_name


class ViewStatus(models.Model):
    status_name = models.CharField(max_length=64)

    def __str__(self):
        return self.status_name


class Status(models.Model):
    status_name = models.CharField(max_length=64)

    def __str__(self):
        return self.status_name


class Genre(models.Model):
    genre_name = models.CharField(max_length=64)

    def __str__(self):
        return self.genre_name


class Anime(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    release_date = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, related_name='animes', blank=True)

    def __str__(self):
        return self.title
