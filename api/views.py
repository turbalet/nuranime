from django.db.models import Avg
from django.http import JsonResponse
from rest_framework import generics
from api.serializers import *
from django.utils import timezone
from rest_framework import authentication, permissions
from rest_framework.filters import SearchFilter, OrderingFilter


class AnimeCreateView(generics.ListCreateAPIView):
    search_fields = ['title']
    filter_backends = (SearchFilter, OrderingFilter)
    serializer_class = AnimeListSerializer

    def get_queryset(self):
        queryset = Anime.objects.all()
        genre = self.request.query_params.get('genre')

        if genre:
            queryset = queryset.filter(genres__genre_name__contains=genre)
        return queryset


class TopAnimeListView(generics.ListAPIView):
    serializer_class = AnimeListSerializer
    queryset = Anime.objects.annotate(avg_rate=Avg('rating__stars')).order_by('-avg_rate')[:20]


class AnimeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnimeSerializer
    queryset = Anime.objects.all()


class GenreCreateView(generics.ListCreateAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class RatingListView(generics.ListAPIView):
    serializer_class = RatingSerializer

    def get_queryset(self):
        queryset = Rating.objects.all()
        anime_id = self.kwargs['anime_id']
        if anime_id is not None:
            queryset = queryset.filter(anime_id=anime_id)
        return queryset


class RatingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()


class RatingCreateView(generics.CreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if (user := self.request.user) and \
                (anime := request.data.get("anime_id")) and (stars := request.data.get("stars")):
            request.data['anime'] = anime
            request.data['user'] = user.id
            request.data['stars'] = stars
            try:
                rating = Rating.objects.get(user=user.id, anime=anime)
                rating.set_stars(stars)
                rating.save()
                data = {"anime": rating.anime_id, "user": rating.user_id, "stars": rating.stars}
                return JsonResponse(data)
            except Rating.DoesNotExist:
                return self.create(request, *args, **kwargs)


class UserView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserAnimeViewStatusCreateView(generics.CreateAPIView):
    serializers_class = UserAnimeViewStatusSerializer
    queryset = UserAnimeViewStatus.objects.all()


class UserAnimeViewStatusListView(generics.ListAPIView):
    serializer_class = UserAnimeViewStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = UserAnimeViewStatus.objects.all()
        user = self.request.user
        list_id = self.kwargs['list_id']
        if list_id is not None:
            queryset = queryset.filter(user=user, view_status_id=list_id)
        return queryset


class UserAnimeViewStatusDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializers_class = UserAnimeViewStatusSerializer
    queryset = UserAnimeViewStatus.objects.all()


class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all()
        anime_id = self.kwargs['anime_id']
        if anime_id is not None:
            queryset = queryset.filter(anime_id=anime_id)
        return queryset


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    # django timezone
    def post(self, request, *args, **kwargs):
        if (message := request.data.get("message")) and (
                user := self.request.user
        ) and (anime_id := request.data.get("anime_id")):
            comment = Comment()
            comment.user = user
            comment.commented_date = timezone.now()
            anime = Anime.objects.get(pk=anime_id)
            comment.anime = anime
            comment.message = message
            comment.save()

            # request.data['commented_date'] = timezone.now()
            # request.data['user'] = user.id
            # request.data['anime'] = anime
            # request.data['message'] = message
        # return self.create(request, *args, **kwargs)
        return JsonResponse("Comment was successfully added", safe=False)


class SubCommentListView(generics.ListAPIView):
    serializer_class = SubCommentSerializer

    def get_queryset(self):
        queryset = SubComment.objects.all()
        comment_id = self.kwargs['comment_id']
        if comment_id is not None:
            queryset = queryset.filter(comment_id=comment_id)
        return queryset


class SubCommentCreateView(generics.CreateAPIView):
    serializer_class = SubCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if (message := request.data.get("message")) and (
                user := self.request.user
        ) and (
                comment := request.data.get("comment_id")
        ):
            request.data['commented_date'] = timezone.now()
            request.data['user'] = user.id
            request.data['message'] = message
            request.data['comment'] = comment
        return self.create(request, *args, **kwargs)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer
