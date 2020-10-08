from django.shortcuts import get_object_or_404
from django.db.models import Avg
from django.db import IntegrityError
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.exceptions import ParseError
from rest_framework import viewsets, filters, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.serializers import (
    CommentSerializer,
    ReviewSerializer,
    UserSerializer,
    CategorySerializer,
    GenreSerializer,
    TitleReadSerializer,
    TitleWriteSerializer,
)

from api.model.feedback import Comment, Review, User
from api.model.content import Categories, Genres, Titles

from api.permissions import IsOwnerOrReadOnly
from api.permissions import AdminResourcePermission, StaffResourcePermission, ReviewCreatePermission, \
    SiteAdminPermission

from api.filters import TitleFilter


# CONTENT


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']
    permission_classes = [IsAuthenticatedOrReadOnly, AdminResourcePermission]


class CategoryDestroyAPIView(generics.DestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, AdminResourcePermission]
    lookup_field = 'slug'


class GenreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']
    permission_classes = [IsAuthenticatedOrReadOnly, AdminResourcePermission]


class GenreDestroyAPIView(generics.DestroyAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly, AdminResourcePermission]


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all().annotate(rating=Avg('reviews__score'))
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitleFilter

    permission_classes = [IsAuthenticatedOrReadOnly, AdminResourcePermission]

    def get_serializer_class(self):
        if self.request.method in ['PATCH', 'POST']:
            return TitleWriteSerializer
        return TitleReadSerializer


# REVIEW


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [

        SiteAdminPermission

    ]

    def get_permissions(self):
        if self.request.method == 'PATCH':
            self.permission_classes = (IsOwnerOrReadOnly,)
        return super(CommentViewSet, self).get_permissions()

    def get_queryset(self):
        return Comment.objects.filter(review=self.kwargs['review_pk'])

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs['review_pk'])
        serializer.save(author=self.request.user, review=review)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [

        SiteAdminPermission

    ]

    def get_permissions(self):
        if self.request.method == 'PATCH':
            self.permission_classes = (IsOwnerOrReadOnly,)
        return super(ReviewViewSet, self).get_permissions()

    def get_queryset(self):
        return Review.objects.filter(title=self.kwargs['id'])

    def perform_create(self, serializer):
        title = get_object_or_404(Titles, pk=self.kwargs['id'])

        try:
            serializer.save(author=self.request.user, title=title)
        except IntegrityError:
            raise ParseError(detail="Автор уже отставил свой обзор на этот пост")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]
