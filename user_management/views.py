from random import choice
from string import ascii_letters, ascii_uppercase

from django.db import IntegrityError
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action

from .models import User
from .permissions import SiteAdminPermission
from .serializers import UserSerializer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class GetTokenAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        user = get_object_or_404(User, email=email)
        code = request.data.get('confirmation_code')
        if user.auth_code == code:
            tokens = get_tokens_for_user(user)
            return Response(tokens, status.HTTP_200_OK)
        return Response({"message": "неверный код подтверждения."},
                        status.HTTP_400_BAD_REQUEST)


class EmailConfirmationAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response(status.HTTP_400_BAD_REQUEST)

        code = ''.join(choice(ascii_uppercase) for i in range(9))
        username = 'User_' + ''.join(choice(ascii_letters) for i in range(6))
        role = request.data.get('role')
        try:
            user = User.objects.create(
                email=email,
                username=username,
                auth_code=code,
                role=role,
            )
        except IntegrityError:
            user = User.objects.get(email=email)
            user.auth_code = code
            username = user.username
        user.save()

        send_mail(
            subject='Ваш код аутентификации в Yamdb',
            message='Сохраните код! Он понадобится вам для получения токена.\n'
                    f'confirmation_code: {code}\n'
                    f'username: {username}',
            recipient_list=[email],
            fail_silently=False,
        )
        return Response({"message": "код был отправлен на указанную почту: "
                                    f"{email}"}, status.HTTP_200_OK)


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = [IsAuthenticated, SiteAdminPermission]

    def get_permissions(self):
        if self.action in ('profile', None):
            return [IsAuthenticated()]
        return super().get_permissions()

    def perform_update(self, serializer):
        serializer.save(data=self.request.data)

    @action(methods=['GET', 'PATCH'], detail=True)
    def profile(self, request):
        if request.method == 'PATCH':
            user = get_object_or_404(User, username=request.user.username)
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(email=user.email, role=user.role)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
