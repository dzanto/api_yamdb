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


class TitleSerializer(serializers.ModelSerializer):
    # rating = serializers.DecimalField(read_only=True, max_digits=10,
    #                                   decimal_places=1, coerce_to_string=False)
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)

    # category = serializers.SlugRelatedField(
    #     queryset=Categories.objects.all(),
    #     slug_field='slug',
    # )
    # genre = serializers.SlugRelatedField(
    #     queryset=Genres.objects.all(),
    #     slug_field='slug', many=True
    # )

    class Meta:
        fields = '__all__'
        model = Titles


class UpdateTitleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Categories.objects.all(),
        slug_field='slug',
    )
    genre = serializers.SlugRelatedField(
        queryset=Genres.objects.all(),
        slug_field='slug', many=True
        
    )

    class Meta:
        fields = '__all__'
        model = Titles
