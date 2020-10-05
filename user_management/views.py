from random import choice
from string import ascii_letters, ascii_uppercase

from django.db import IntegrityError
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


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
            return Response({"message": tokens})
        return Response({"message": "неверный код подтверждения."})


class EmailConfirmationAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        code = ''.join(choice(ascii_uppercase) for i in range(9))
        username = 'User#' + ''.join(choice(ascii_letters) for i in range(6))
        try:
            user = User.objects.create(
                email=email,
                username=username,
                auth_code=code
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
            from_email=None,
            recipient_list=[email],
            fail_silently=False,
        )
        return Response({"message": "код был отправлен на указанную почту: "
                                    f"{email}"})
