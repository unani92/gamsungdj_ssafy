from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

User = get_user_model()
from .serializers import UserSerializer
from .models import UserProfile


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter


class UserAPI(APIView):

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def post(self, request, format=None):
        user = request.user
        try:
            UserProfile.objects.get(user=user)
            return Response(status=status.HTTP_409_CONFLICT)
        except UserProfile.DoesNotExist:
            profile = UserProfile.objects.create(
                user=user,
                age=request.data.get('age'),
                gender=request.data.get('gender'),
                avatar=request.data.get('avatar'),
                is_signed_up=True
            )
            serializer = UserSerializer(user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

