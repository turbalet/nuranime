from rest_framework import serializers
from api.models import *


class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['-id']
        model = Studio
        fields = '__all__'


class ViewStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewStatus
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'
        extra_kwargs = {'genres': {'required': False}}
        depth = 1


class GenreSerializer(serializers.ModelSerializer):
    animes = AnimeSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = '__all__'
        extra_kwargs = {'animes': {'required': False}}


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
