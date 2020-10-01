from rest_framework import serializers
from api.model.content import Categories, Genres, Titles


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Categories


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Genres


class TitleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Categories.objects.all(),
        slug_field='slug'
    )
    genre = serializers.SlugRelatedField(
        queryset=Genres.objects.all(),
        slug_field='slug', many=True
        
    )

    class Meta:
        fields = '__all__'
        model = Titles
