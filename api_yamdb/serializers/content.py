from rest_framework import serializers

from api_yamdb.models.content import Categories, Genres, Titles


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Categories


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Genres


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Titles
