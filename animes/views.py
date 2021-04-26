# from rest_framework import generics
# from animes.serializers import *
# from animes.models import Studio
# from django_filters.rest_framework import DjangoFilterBackend
#
#
# class StudioCreateView(generics.CreateAPIView):
#     serializer_class = StudioSerializer
#
#
# class StudioListView(generics.ListAPIView):
#     serializer_class = StudioListSerializer
#     queryset = Studio.objects.all()
#
#
# class StudioDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = StudioSerializer
#     queryset = Studio.objects.all()
#
# class ViewStatusCreateView(generics.CreateAPIView):
#     serializer_class = ViewStatusSerializer
#
# class ViewStatusListView(generics.ListAPIView):
#     serializer_class = ViewStatusListSerializer
#     queryset = ViewStatus.objects.all()
#
# class ViewStatusDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ViewStatusSerializer
#     queryset = ViewStatus.objects.all()
#
# class StatusCreateView(generics.CreateAPIView):
#     serializer_class = StatusSerializer
#
# class StatusListView(generics.ListAPIView):
#     serializer_class = StatusListSerializer
#     queryset = Status.objects.all()
#
# class StatusDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = StatusSerializer
#     queryset = Status.objects.all()
#
# class CategoryCreateView(generics.CreateAPIView):
#     serializer_class = CategorySerializer
#
# class CategoryListView(generics.ListAPIView):
#     serializer_class = CategoryListSerializer
#     queryset = Category.objects.all()
#
# class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()
#
# class AnimeCreateView(generics.CreateAPIView):
#     serializer_class = AnimeSerializer
#
# class AnimeListView(generics.ListAPIView):
#     serializer_class = AnimeListSerializer
#     queryset = Anime.objects.all()
#
# class AnimeDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = AnimeSerializer
#     queryset = Anime.objects.all()
#
# class AnimeCategoryCreateView(generics.CreateAPIView):
#     serializer_class = AnimeCategorySerializer
#
# class AnimeCategoryListView(generics.ListAPIView):
#     serializer_class = AnimeCategoryListSerializer
#     queryset = AnimeCategory.objects.all()
#     lookup_field = 'anime'
#
# class AnimeCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = AnimeCategorySerializer
#     queryset = AnimeCategory.objects.all()
#
# class CommentCreateView(generics.CreateAPIView):
#     serializer_class = CommentSerializer
#
#
#
# class CommentListView(generics.ListAPIView):
#     serializer_class = CommentListSerializer
#     queryset = Comment.objects.all()
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
# class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = CommentSerializer
#     queryset = Comment.objects.all()
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
# class SubCommentCreateView(generics.CreateAPIView):
#     serializer_class = SubCommentSerializer
#
# class SubCommentListView(generics.ListAPIView):
#     serializer_class = SubCommentListSerializer
#     queryset = SubComment.objects.all()
#
# class SubCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = SubCommentSerializer
#     queryset = SubComment.objects.all()
#
# class FavouriteCreateView(generics.CreateAPIView):
#     serializer_class = FavouriteSerializer
#
# class FavouriteListView(generics.ListAPIView):
#     serializer_class = FavouriteListSerializer
#     queryset = Favourite.objects.all()
#
# class FavouriteDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = FavouriteSerializer
#     queryset = Favourite.objects.all()
#
# class UserAnimeCreateView(generics.CreateAPIView):
#     serializer_class = UserAnimeSerializer
#
# class UserAnimeListView(generics.ListAPIView):
#     serializer_class = UserAnimeListSerializer
#     queryset = UserAnime.objects.all()
#
# class UserAnimeDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = UserAnimeSerializer
#     queryset = UserAnime.objects.all()