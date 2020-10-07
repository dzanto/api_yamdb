from rest_framework import viewsets, filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from api.model.content import Categories, Genres, Titles
from api.serializer.content import CategorySerializer, GenreSerializer, TitleReadSerializer, TitleWriteSerializer
from api.permissions import AdminResourcePermission, ReviewCreatePermission, IsOwnerOrReadOnly, StaffResourcePermission, IsAdminOrReadOnly
from django.db.models import Avg
from api.filters import TitleFilter
from rest_framework.generics import get_object_or_404


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']
    permission_classes = [IsAdminOrReadOnly]


class CategoryDestroyAPIView(generics.DestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AdminResourcePermission, IsAuthenticated]
    lookup_field = 'slug'


class GenreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']
    permission_classes = [AdminResourcePermission, IsAuthenticatedOrReadOnly]


class GenreDestroyAPIView(generics.DestroyAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AdminResourcePermission, IsAuthenticated]
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all().annotate(rating=Avg('reviews__score'))
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitleFilter

    permission_classes = (IsAuthenticatedOrReadOnly, AdminResourcePermission)

    def get_serializer_class(self):
        if self.request.method in ['PATCH', 'POST']:
            return TitleWriteSerializer
        return TitleReadSerializer
