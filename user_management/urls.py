from django.urls import path

from . import views


urlpatterns = [
    path('v1/auth/email/', views.EmailConfirmationAPIView.as_view()),
    path('v1/auth/token/', views.GetTokenAPIView.as_view()),
]
