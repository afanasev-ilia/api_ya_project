from django.db.models import QuerySet
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.serializers import Serializer

from api.permissions import IsAuthorOrReadOnly
from api.serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)
from posts.models import Group, Post


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer: Serializer) -> None:
        serializer.save()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('group', 'author')
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(
        self,
        serializer: Serializer,
    ) -> None:
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = CommentSerializer

    def get_post(self, request: HttpRequest) -> Post:
        del request
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self) -> QuerySet:
        return self.get_post(self).comments.select_related('post')

    def perform_create(
        self,
        serializer: Serializer,
    ) -> None:
        serializer.save(author=self.request.user, post=self.get_post(self))


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self) -> QuerySet:
        return self.request.user.follower.select_related('following')

    def perform_create(self, serializer: Serializer) -> None:
        serializer.save(user=self.request.user)
