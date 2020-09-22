from rest_framework import viewsets, filters, generics
from api.model.content import Categories, Genres, Titles
from api.serializer.content import CategorySerializer, GenreSerializer, TitleSerializer
from rest_framework.permissions import IsAdminUser
from api.permissions import AdminResourcePermission


# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Categories.objects.all()
#     serializer_class = CategorySerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['=name']
#     permission_classes = [AdminResourcePermission]


class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']
    permission_classes = [AdminResourcePermission]


# class CategoryCreateAPIView(generics.CreateAPIView):
#     queryset = Categories.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [AdminResourcePermission]


class CategoryDestroyAPIView(generics.DestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AdminResourcePermission]



# class GenreViewSet(viewsets.ModelViewSet):
#     queryset = Genres.objects.all()
#     serializer_class = GenreSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['=name']


class GenreListAPIView(generics.ListCreateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']
    permission_classes = [AdminResourcePermission]


# class GenreCreateAPIView(generics.CreateAPIView):
#     queryset = Genres.objects.all()
#     serializer_class = GenreSerializer
#     permission_classes = [AdminResourcePermission]



class GenreDestroyAPIView(generics.DestroyAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AdminResourcePermission]




class TitleViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [AdminResourcePermission]
