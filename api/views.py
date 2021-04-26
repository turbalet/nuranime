from django.shortcuts import render
from rest_framework import generics
from api.serializers import *


# Create your views here.


class AnimeCreateView(generics.ListCreateAPIView):
    serializer_class = AnimeSerializer
    queryset = Anime.objects.all()


class AnimeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnimeSerializer
    queryset = Anime.objects.all()


class GenreCreateView(generics.ListCreateAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class UserView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
