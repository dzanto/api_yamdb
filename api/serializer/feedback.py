from rest_framework import serializers 
from api.model.feedback import Comment, Review, User
from rest_framework.validators import UniqueTogetherValidator


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
        slug_field='name' 
    ) 

    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True, 
        default=serializers.CurrentUserDefault()
    )
    
    
    class Meta: 
        fields = ('text', 'score', 'title', 'author')
        model = Review



class UserSerializer(serializers.ModelSerializer):
    
   
    class Meta: 
        fields = '__all__' 
        model = User
        