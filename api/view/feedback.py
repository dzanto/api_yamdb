from rest_framework import viewsets, filters, permissions, generics, status
from rest_framework.viewsets import ViewSetMixin
from django.shortcuts import get_object_or_404 
from api.serializer.feedback import CommentSerializer, ReviewSerializer, UserSerializer
from api.model.feedback import Comment, Review, User
from api.model.content import Titles
from api.permissions import IsOwnerOrReadOnly 
from rest_framework.exceptions import ParseError
from django.db import IntegrityError

 

class CommentViewSet(viewsets.ModelViewSet): 
    serializer_class = CommentSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, 
                          IsOwnerOrReadOnly] 
     
    def get_queryset(self): 
        return Comment.objects.filter(review=self.kwargs['review_pk']) 
         
    def perform_create(self, serializer):  
       review = get_object_or_404(Review, pk=self.kwargs['review_pk']) 
       serializer.save(author=self.request.user,  review=review)  


class ReviewViewSet(viewsets.ModelViewSet): 
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, 
                          IsOwnerOrReadOnly] 
     
    def get_queryset(self): 
        return Review.objects.filter(title=self.kwargs['id']) 
         
    def perform_create(self, serializer):  
        title = get_object_or_404(Titles, pk=self.kwargs['id'])
        
        serializer.save(author=self.request.user, title=title) 
        
class UserViewSet(viewsets.ModelViewSet): 
    queryset=User.objects.all()
    serializer_class = UserSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, 
                          IsOwnerOrReadOnly] 
     
    
