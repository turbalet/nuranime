# from django.db import models
# from django.contrib.auth import get_user_model
#
# User = get_user_model()
#
# class Studio(models.Model):
#     studio_id = models.BigAutoField(primary_key=True)
#     studio_name = models.CharField(max_length=64)
#
#     def __str__(self):
#         return self.studio_name
#
#
# class ViewStatus(models.Model):
#     status_id = models.BigAutoField(primary_key=True)
#     status_name = models.CharField(max_length=64)
#
#     def __str__(self):
#         return self.status_name
#
#
# class Status(models.Model):
#     status_id = models.BigAutoField(primary_key=True)
#     status_name = models.CharField(max_length=64)
#
#     def __str__(self):
#         return self.status_name
#
# class Category(models.Model):
#     category_id = models.BigAutoField(primary_key=True)
#     category_name = models.CharField(max_length=64)
#
#     def __str__(self):
#         return self.category_name
#
# class Anime(models.Model):
#     anime_id = models.BigAutoField(primary_key=True)
#     title = models.CharField(max_length=250)
#     description = models.TextField()
#     year = models.IntegerField()
#     season = models.CharField(max_length=10)
#     status = models.ForeignKey(Status, on_delete=models.CASCADE)
#     studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title
#
# class AnimeCategory(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#
# class Comment(models.Model):
#     comment_id = models.BigAutoField(primary_key=True)
#     message = models.TextField()
#     commented_date = models.DateField()
#     anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
#     user = User
#
# class SubComment(models.Model):
#     subcomment_id = models.BigAutoField(primary_key=True)
#     message = models.TextField()
#     commented_date = models.DateField()
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
#     user = User
#     anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
#
# class Favourite(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
#     user = User
#
# class UserAnime(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
#     user = User
#     status = models.ForeignKey(ViewStatus, on_delete=models.CASCADE)
