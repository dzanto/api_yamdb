from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from api.view import content


router = DefaultRouter()
router.register('categories', content.CategoryViewSet)
router.register('genres', content.GenreViewSet)
router.register('titles', content.TitleViewSet)

urlpatterns = [
    path('v1/group/', views.GroupAPIView.as_view()),
    path('v1/follow/', views.FollowAPIView.as_view()),
    path('v1/', include(router.urls)),
]