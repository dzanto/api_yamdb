from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.view import content as views

router = DefaultRouter()
router.register('categories', views.CategoryViewSet)
router.register('genres', views.GenreViewSet)
router.register('titles', views.TitleViewSet)
