from rest_framework import serializers
from api.model.content import Categories, Genres, Titles
from rest_framework.validators import UniqueValidator


class CategorySerializer(serializers.ModelSerializer):
    # slug = serializers.SlugRelatedField(
    #     queryset=Categories.objects.all(),
    #     slug_field='slug',
    #     validators=[UniqueValidator(queryset=Categories.objects.all())])

    class Meta:
        fields = ['name', 'slug']
        model = Categories


class GenreSerializer(serializers.ModelSerializer):
    # slug = serializers.SlugRelatedField(
    #     queryset=Genres.objects.all(),
    #     slug_field='slug',
    #     validators=[UniqueValidator(queryset=Genres.objects.all())])

    class Meta:
        fields = ['name', 'slug']
        model = Genres


class TitleSerializer(serializers.ModelSerializer):
    rating = serializers.CharField()
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)
    # category = serializers.StringRelatedField(
    #     # queryset=Categories.objects.all(),
    #     # slug_field='slug'
    # )
    # genre = serializers.SlugRelatedField(
    #     queryset=Genres.objects.all(),
    #     slug_field='slug', many=True
    # )

    class Meta:
        fields = '__all__'
        model = Titles
