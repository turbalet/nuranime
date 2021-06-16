from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.functions import Coalesce
from django.conf import settings


def manga_chapter_upload_location(instance, filename):
    # /media/Manga_Name/Chapter_Number/
    return 'mangas/{}/{}/{}'.format(
        str(instance.chapter.manga.eng_title).replace(" ", "_").replace(":", " ").replace("/", "").replace("\\", ""),
        instance.chapter.chapter_no, filename)


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


class Manga(models.Model):
    title = models.CharField(max_length=64)
    eng_title = models.CharField(max_length=64, default='F')
    description = models.TextField()
    release_date = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    author = models.CharField(max_length=64)
    artist = models.CharField(max_length=64)
    poster = models.ImageField(upload_to='posters/', default='NULL')
    genres = models.ManyToManyField(Genre, related_name='mangas', blank=True)

    def __str__(self):
        return self.title

    def avg_rating(self):
        return Rating.objects.filter(manga=self).aggregate(
            avg=Coalesce(models.Avg('stars'), 0),
        )

    def count_rate(self):
        return Rating.objects.filter(manga=self).count()


class Anime(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    release_date = models.DateField()
    season = models.CharField(max_length=64)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    poster = models.ImageField(upload_to='posters/', default='NULL')
    genres = models.ManyToManyField(Genre, related_name='animes', blank=True)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, blank=True, default=None)

    def __str__(self):
        return self.title

    def avg_rating(self):
        return Rating.objects.filter(anime=self).aggregate(
            avg=Coalesce(models.Avg('stars'), 0),
        )

    def count_rate(self):
        return Rating.objects.filter(anime=self).count()


# class User(AbstractUser):
#     user_img = models.ImageField(upload_to='users_img/', default='NULL')
#
#     def __str__(self):
#         return self.username


class UserAnimeViewStatus(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    view_status = models.ForeignKey(ViewStatus, on_delete=models.CASCADE)


class UserMangaViewStatus(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    view_status = models.ForeignKey(ViewStatus, on_delete=models.CASCADE)


class Comment(models.Model):
    message = models.TextField()
    commented_date = models.DateTimeField()
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, blank=True, default=None)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, blank=True, default=None)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class SubComment(models.Model):
    message = models.TextField()
    commented_date = models.DateTimeField()
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Chapter(models.Model):
    title = models.CharField(max_length=64)
    release_date = models.DateField()
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    chapter_no = models.CharField(max_length=64)

    def __str__(self):
        return self.manga.title + ': Chapter ' + self.chapter_no


class ChapterFiles(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    chapter_images = models.FileField(upload_to=manga_chapter_upload_location)
    page_no = models.IntegerField()


class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, blank=True)
    stars = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, blank=True)

    def set_stars(self, stars):
        self.stars = stars


class Episode(models.Model):
    episode_number = models.IntegerField()
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    video = models.FileField(upload_to='episodes/', default='NULL')
