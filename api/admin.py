from django.contrib import admin
from api.models import *
from users.models import User
# Register your models here.

admin.site.register(Studio)
admin.site.register(Status)
admin.site.register(ViewStatus)
admin.site.register(Genre)
admin.site.register(Anime)
admin.site.register(Comment)
admin.site.register(SubComment)
admin.site.register(Rating)
admin.site.register(Episode)
admin.site.register(Chapter)
admin.site.register(Manga)
admin.site.register(ChapterFiles)
