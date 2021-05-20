from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from users.models import User
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
        fields = ['id', 'title', 'description', 'release_date', 'status', 'studio', 'poster', 'genres', 'avg_rating',
                  'count_rate']
        extra_kwargs = {'genres': {'required': False}}
        depth = 1


class AnimeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ('id', 'title', 'release_date', 'poster', 'avg_rating', 'count_rate',)
        extra_kwargs = {'genres': {'required': False}}


class GenreSerializer(serializers.ModelSerializer):
    animes = AnimeSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = '__all__'
        extra_kwargs = {'animes': {'required': False}}


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 1


class SubCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubComment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class UserAnimeViewStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnimeViewStatus
        fields = '__all__'
        depth = 1


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
