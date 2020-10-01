from rest_framework import serializers
from api.model.content import Categories, Genres, Titles
from rest_framework.validators import UniqueValidator


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Categories
        validators = [UniqueValidator(
            queryset=Categories.objects.all()
        )]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Genres
        validators = [UniqueValidator(
            queryset=Genres.objects.all()
        )]


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
