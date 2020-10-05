from django_filters import rest_framework as filters
from api.model.content import Titles
from django_filters import rest_framework as filters
    
class TitleFilter(filters.FilterSet):
    genre = filters.CharFilter(field_name='genre__slug', lookup_expr='iexact')
    category = filters.CharFilter(field_name="category__slug")
    name = filters.CharFilter(field_name="name", lookup_expr="contains")
    year = filters.NumberFilter(field_name="year", lookup_expr="iexact")

    class Meta:
        model = Titles
        fields = ['genre','category','name','year'] 