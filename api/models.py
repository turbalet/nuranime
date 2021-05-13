from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.functions import Coalesce


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

    def avg_rating(self):
        return Rating.objects.filter(anime=self).aggregate(
            avg=Coalesce(models.Avg('stars'), 0),
        )

    def count_rate(self):
        return Rating.objects.filter(anime=self).count()


class User(AbstractUser):
    user_img = models.ImageField(upload_to='users_img/', default='NULL')

    def __str__(self):
        return self.username


class UserAnimeViewStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    view_status = models.ForeignKey(ViewStatus, on_delete=models.CASCADE)


class Comment(models.Model):
    message = models.TextField()
    commented_date = models.DateTimeField()
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class SubComment(models.Model):
    message = models.TextField()
    commented_date = models.DateTimeField()
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])

    def set_stars(self, stars):
        self.stars = stars
