from django.urls import path
# from rest_framework_simplejwt.views import (
#         TokenObtainPairView,
#         TokenRefreshView,
#     )
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
router.register('users', UserViewSet)   

urlpatterns = [
        # path(
        #     'v1/token/',
        #     TokenObtainPairView.as_view(),
        #     name='token_obtain_pair'
        # ),
        # path(
        #     'v1/token/refresh/',
        #     TokenRefreshView.as_view(),
        #     name='token_refresh'
        # ),
        path('v1/', include(router.urls)),   
    ]
