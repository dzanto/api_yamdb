from rest_framework import viewsets, filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from api.model.content import Categories, Genres, Titles
from api.serializer.content import CategorySerializer, GenreSerializer, TitleReadSerializer, TitleWriteSerializer
from api.permissions import AdminResourcePermission
from django.db.models import Avg
from api.filters import TitleFilter


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']
    # permission_classes = [AdminResourcePermission]


class CategoryDestroyAPIView(generics.DestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    # permission_classes = [AdminResourcePermission]


class GenreListCreateAPIView(generics.ListCreateAPIView):
    
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']
    # permission_classes = [AdminResourcePermission]


class GenreDestroyAPIView(generics.DestroyAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'slug'
    # permission_classes = [AdminResourcePermission]


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all().annotate(rating=Avg('reviews__score'))
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitleFilter
    
    # permission_classes = [AdminResourcePermission]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TitleWriteSerializer
        elif self.request.method == 'PATCH':
            return TitleWriteSerializer
        return TitleReadSerializer