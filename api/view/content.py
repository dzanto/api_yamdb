from rest_framework import viewsets, filters
from api.model.content import Categories, Genres, Titles
from api.serializer.content import CategorySerializer, GenreSerializer, TitleSerializer
from rest_framework.pagination import PageNumberPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']
    # pagination_class = PageNumberPagination


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']
    # pagination_class = PageNumberPagination


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitleSerializer
