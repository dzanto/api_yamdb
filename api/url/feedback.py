from django.urls import include, path
from rest_framework.authtoken import views 
from rest_framework.routers import DefaultRouter 
from api import views
 

router = DefaultRouter() 

router.register(
    'titles/(?P<id>\d+)/reviews/(?P<review_pk>\d+)/comments', 
    views.CommentViewSet, basename ='perform_create_comments'
)
router.register(
    'titles/(?P<id>\d+)/reviews', 
    views.ReviewViewSet, basename ='perform_create_reviews'
)

urlpatterns = [
        path('v1/', include(router.urls)),
    ]
