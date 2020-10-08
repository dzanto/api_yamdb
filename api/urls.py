from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('titles', views.TitleViewSet)
router.register(
    'titles/(?P<id>\d+)/reviews/(?P<review_pk>\d+)/comments',
    views.CommentViewSet, basename='perform_create_comments'
)
router.register(
    'titles/(?P<id>\d+)/reviews',
    views.ReviewViewSet, basename='perform_create_reviews'
)

urlpatterns = [
    path('v1/categories/', views.CategoryListCreateAPIView.as_view()),
    path('v1/categories/<slug:slug>/', views.CategoryDestroyAPIView.as_view()),
    path('v1/genres/', views.GenreListCreateAPIView.as_view()),
    path('v1/genres/<slug:slug>/', views.GenreDestroyAPIView.as_view()),
    path('v1/', include(router.urls)),
]
