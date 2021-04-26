# from rest_framework import serializers
# from animes.models import *
#
# class StudioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Studio
#         fields = '__all__'
#
#
# class StudioListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Studio
#         fields = '__all__'
#
# class ViewStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ViewStatus
#         fields = '__all__'
#
# class ViewStatusListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ViewStatus
#         fields = '__all__'
#
# class StatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Status
#         fields = '__all__'
#
# class StatusListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Status
#         fields = '__all__'
#
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'
#
# class CategoryListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'
#
# class AnimeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Anime
#         fields = '__all__'
#
# class AnimeListSerializer(serializers.ModelSerializer):
#     status = serializers.SlugRelatedField(read_only=True, slug_field='status_name')
#     studio = serializers.SlugRelatedField(read_only=True, slug_field='studio_name')
#     class Meta:
#         model = Anime
#         fields = '__all__'
#
# class AnimeCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AnimeCategory
#         fields = '__all__'
#
# class AnimeCategoryListSerializer(serializers.ModelSerializer):
#     category = serializers.SlugRelatedField(read_only=True, slug_field='category_name')
#     anime = serializers.SlugRelatedField(read_only=True, slug_field='title')
#     class Meta:
#         model = AnimeCategory
#         fields = '__all__'
#
# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'
#
# class CommentListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'
#
# class SubCommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubComment
#         fields = '__all__'
#
# class SubCommentListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubComment
#         fields = '__all__'
#
# class FavouriteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Favourite
#         fields = '__all__'
#
# class FavouriteListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Favourite
#         fields = '__all__'
#
# class UserAnimeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserAnime
#         fields = '__all__'
#
# class UserAnimeListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserAnime
#         fields = '__all__'
#
