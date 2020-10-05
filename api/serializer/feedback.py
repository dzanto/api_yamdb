from rest_framework import serializers 
from api.model.feedback import Comment, Review, User
from api.model.content import Titles
from rest_framework.validators import UniqueTogetherValidator
from django.core.exceptions import ValidationError


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
        fields = ('text', 'score', 'title', 'author')
        model = Review
    


class UserSerializer(serializers.ModelSerializer):
    
   
    class Meta: 
        fields = '__all__' 
        model = User
        