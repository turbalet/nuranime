from django.urls import path
from api.views import *

urlpatterns = [
    path('animes/', AnimeCreateView.as_view()),  # get all animes
    path('animes/top', TopAnimeListView.as_view()),  # get all animes
    path('anime/detail/<int:pk>/', AnimeDetailView.as_view()),  # get detail info about anime
    path('genres/', GenreCreateView.as_view()),  # get all genres
    path('genre/detail/<int:pk>/', GenreDetailView.as_view()),  # get detail info about genre
    path('users/', UserView.as_view()),
    # get user's view statuses of anime by viewstatus id
    path('profile/anime-list/', UserAnimeViewStatusCreateView.as_view()),
    path('profile/manga-list/', UserMangaViewStatusCreateView.as_view()),
    path('viewstatuses', ViewStatusListView.as_view()),
    path('profile/anime-list/<int:list_id>', UserAnimeViewStatusListView.as_view()),
    path('profile/manga-list/<int:list_id>', UserMangaViewStatusListView.as_view()),
    path('comments/', CommentCreateView.as_view()),  # get all comments
    path('comments/anime/<int:anime_id>/', AnimeCommentListView.as_view()),  # get all comments of anime
    path('comments/manga/<int:manga_id>/', MangaCommentListView.as_view()),
    path('subcomments/', SubCommentCreateView.as_view()),  # get all sub comments
    path('subcomments/<int:comment_id>/', SubCommentListView.as_view()),  # get sub comments of comment
    path('rating/', RatingCreateView.as_view()),  # get all ratings or rate anime
    path('rating/anime/<int:anime_id>', RatingListView.as_view()),  # get rates of anime by anime id
    path('rating/detail/<int:pk>', RatingDetailView.as_view()),  # get detail info about specific rate
    path('episodes/<int:anime_id>/', EpisodeListView.as_view()),
    path('mangas/', MangaListCreateView.as_view()),
    path('mangas/top', TopMangaListView.as_view()),
    path('manga/detail/<int:pk>', MangaDetailView.as_view()),
    path('manga/chapter/detail/<int:pk>', ChapterDetailView.as_view()),
    path('manga/chapters/<int:manga_id>', ChapterListCreateView.as_view()),
    path('manga/pages/<int:chapter_id>', ChapterFilesListCreateView.as_view())
]
