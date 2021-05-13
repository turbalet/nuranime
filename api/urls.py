from django.urls import path
from api.views import *

urlpatterns = [
    path('animes/', AnimeCreateView.as_view()),  # get all animes
    path('anime/detail/<int:pk>/', AnimeDetailView.as_view()),  # get detail info about anime
    path('genres/', GenreCreateView.as_view()),  # get all genres
    path('genre/detail/<int:pk>/', GenreDetailView.as_view()),  # get detail info about genre
    path('users/', UserView.as_view()),
    # get user's view statuses of anime by viewstatus id
    path('profile/anime-list/<int:list_id>', UserAnimeViewStatusListView.as_view()),
    path('register/', RegisterView.as_view()),
    path('comments/', CommentCreateView.as_view()),  # get all comments
    path('comments/<int:anime_id>/', CommentListView.as_view()),  # get all comments of anime
    path('subcomments/', SubCommentCreateView.as_view()),  # get all sub comments
    path('subcomments/<int:comment_id>/', SubCommentListView.as_view()),  # get sub comments of comment
    path('rating/', RatingCreateView.as_view()),  # get all ratings
    path('rating/anime/<int:anime_id>', RatingListView.as_view()),  # get rates of anime by anime id
    path('rating/detail/<int:pk>', RatingDetailView.as_view()),  # get detail info about specific rate
]
