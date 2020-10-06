from django.urls import include, path
from rest_framework.authtoken import views 
from rest_framework.routers import DefaultRouter 
from api.view.feedback import ReviewViewSet, CommentViewSet, UserViewSet
 

router = DefaultRouter() 

router.register(
    'titles/(?P<id>\d+)/reviews/(?P<review_pk>\d+)/comments', 
    CommentViewSet, basename ='perform_create_reviews'
)
router.register(
    'titles/(?P<id>\d+)/reviews', 
    ReviewViewSet, basename ='perform_create_reviews'
)

urlpatterns = [
        path('v1/', include(router.urls)),
    ]
