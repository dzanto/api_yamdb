from django_filters import rest_framework as filters
from api.model.content import Titles


class GenreCategoryFilter(filters.FilterSet):
    genre = filters.CharFilter(
        field_name='genre__slug', lookup_expr='iexact'
    )
    category = filters.CharFilter(
        field_name='category__slug', lookup_expr='iexact'
    )
    name = filters.CharFilter(
        field_name='name', lookup_expr='iexact'
    )
    year = filters.NumberFilter(
        field_name='year', lookup_expr='iexact'
    )

    class Meta:
        model = Titles
        fields = ['genre', 'category', 'name', 'year']