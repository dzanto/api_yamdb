from rest_framework import serializers
from api.model.content import Categories, Genres, Titles
from rest_framework.validators import UniqueValidator


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['name', 'slug']
        model = Categories


class GenreSerializer(serializers.ModelSerializer):

        
    class Meta:
        fields = ['name', 'slug']
        model = Genres
        
class TitleWriteSerializer(serializers.ModelSerializer):
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


class TitleReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    genre = GenreSerializer(many=True)
    rating = serializers.IntegerField()
    
    class Meta:
        fields = '__all__'
        model = Titles
