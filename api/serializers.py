from rest_framework import serializers

from api.model.content import Categories, Genres, Titles
from api.model.feedback import Comment, Review, User


# CONTENT


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


# REVIEW


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
    )
    review = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='text'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name',

    )

    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True,
        default=serializers.CurrentUserDefault()
    )

    def create(self, validated_data):
        title = validated_data['title']
        author = validated_data['author']
        message = 'Author already made review on this title'

        if Review.objects.filter(title=title, author=author).exists():
            raise serializers.ValidationError(message)
        return Review.objects.create(**validated_data)

    class Meta:
        fields = ('id', 'text', 'score', 'title', 'author', 'pub_date')
        model = Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User
