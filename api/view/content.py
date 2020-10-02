from rest_framework import viewsets, filters, generics
from api.model.content import Categories, Genres, Titles
from api.serializer.content import CategorySerializer, GenreSerializer, TitleSerializer
from api.permissions import AdminResourcePermission


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']
    # permission_classes = [AdminResourcePermission]


class CategoryDestroyAPIView(generics.DestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AdminResourcePermission]

    def get_object(self):
        obj = get_object_or_404(Categories, slug=self.kwargs.get('slug'))
        return obj
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
    permission_classes = [AdminResourcePermission]

    def get_object(self):
        obj = get_object_or_404(Genres, slug=self.kwargs.get('slug'))
        return obj
    lookup_field = 'slug'
    # permission_classes = [AdminResourcePermission]


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    filter_class = GenreCategoryFilter
    filter_backends = [DjangoFilterBackend]

    def get_serializer_class(self):
        if self.request.method in ['PATCH', 'POST']:
            return UpdateTitleSerializer
        return TitleSerializer

