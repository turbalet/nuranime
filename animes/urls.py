# from django.contrib import admin
# from django.urls import path, include
# from animes.views import *
# urlpatterns = [
#     path('studio/create/', StudioCreateView.as_view()),
#     path('studios/', StudioListView.as_view()),
#     path('studio/detail/<int:pk>/', StudioDetailView.as_view()),
#     path('view-status/create/', ViewStatusCreateView.as_view()),
#     path('view-statuses/', ViewStatusListView.as_view()),
#     path('view-status/detail/<int:pk>/', ViewStatusDetailView.as_view()),
#     path('status/create/', StatusCreateView.as_view()),
#     path('statuses/', StatusListView.as_view()),
#     path('status/detail/<int:pk>/', StatusDetailView.as_view()),
#     path('category/create/', CategoryCreateView.as_view()),
#     path('categories/', CategoryListView.as_view()),
#     path('category/detail/<int:pk>/', CategoryDetailView.as_view()),
#     path('anime/create/', AnimeCreateView.as_view()),
#     path('animes/', AnimeListView.as_view()),
#     path('anime/detail/<int:pk>/', AnimeDetailView.as_view()),
#     path('anime-category/create/', AnimeCategoryCreateView.as_view()),
#     path('anime-categories/<int:pk>/', AnimeCategoryListView.as_view()),
#     path('anime-category/detail/<int:pk>/', AnimeCategoryDetailView.as_view()),
#     path('comment/create/', CommentCreateView.as_view()),
#     path('comments/', CommentListView.as_view()),
#     path('comment/detail/<int:pk>/', CommentDetailView.as_view()),
#     path('subcomment/create/', SubCommentCreateView.as_view()),
#     path('subcomments/', SubCommentListView.as_view()),
#     path('subcomment/detail/<int:pk>/', SubCommentDetailView.as_view()),
#     path('favourite/create/', FavouriteCreateView.as_view()),
#     path('favourites/', FavouriteListView.as_view()),
#     path('favourite/detail/<int:pk>/', FavouriteDetailView.as_view()),
#     path('user-anime/create/', UserAnimeCreateView.as_view()),
#     path('user-animes/', UserAnimeListView.as_view()),
#     path('user-anime/detail/<int:pk>/', UserAnimeDetailView.as_view()),
# ]