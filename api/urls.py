from django.urls import path, include
from api.views import *
urlpatterns = [
        path('animes/', AnimeCreateView.as_view()),
        path('anime/detail/<int:pk>/', AnimeDetailView.as_view()),
        path('genres/', GenreCreateView.as_view()),
        path('genre/detail/<int:pk>/', GenreDetailView.as_view()),
        path('users/', UserView.as_view()),

]