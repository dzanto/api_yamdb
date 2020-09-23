from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.view import content as views

router = DefaultRouter()
router.register('titles', views.TitleViewSet)


urlpatterns = [
    path('v1/categories/', views.CategoryListCreateAPIView.as_view()),
    path('v1/categories/<int:pk>/', views.CategoryDestroyAPIView.as_view()),
    path('v1/genres/', views.GenreListCreateAPIView.as_view()),
    path('v1/genres/<int:pk>/', views.GenreDestroyAPIView.as_view()),
    path('v1/', include(router.urls)),
]
