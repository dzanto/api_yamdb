from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.view import content as views

router = DefaultRouter()
# router.register('categories', views.CategoryViewSet)
# router.register('genres', views.GenreViewSet)
router.register('titles', views.TitleViewSet)


urlpatterns = [
    # path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/categories/', views.CategoryListAPIView.as_view()),
    path('v1/categories/<int:pk>', views.CategoryDestroyAPIView.as_view()),
    path('v1/genres/', views.GenreListAPIView.as_view()),
    path('v1/genres/<int:pk>', views.GenreDestroyAPIView.as_view()),
    path('v1/', include(router.urls)),
]