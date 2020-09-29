from django.shortcuts import render, get_object_or_404
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()
from .serializers import UserSerializer, UserPlayListSerializer, UserProfileSerializer
from .models import UserProfile, UserPlayList


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter


class UserAPI(APIView):
    @permission_classes([IsAuthenticated])
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def post(self, request):
        user = request.user
        try:
            UserProfile.objects.get(user=user)
            return Response(status=status.HTTP_409_CONFLICT)
        except UserProfile.DoesNotExist:
            request.data['user'] = user.id
            serializer = UserProfileSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=user)
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAuthenticated])
    def put(self, request):
        user = request.user
        profile = get_object_or_404(UserProfile, user=user)
        if request.user == profile.user:
            serializer = UserProfileSerializer(profile, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                user_serializer = UserSerializer(user)
                return Response(user_serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class PlaylistAPI(APIView):
    @permission_classes([IsAuthenticated])
    def get(self, request):
        user = request.user
        playlists = user.user_playlists.order_by('-pk')
        serializer = UserPlayListSerializer(playlists, many=True)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def post(self, request):
        user = request.user
        serializer = UserPlayListSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            playlist = serializer.save(user=user)
            if playlist:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlaylistDetailAPI(APIView):
    @permission_classes([IsAuthenticated])
    def get(self, request, pk):
        playlist = get_object_or_404(UserPlayList, pk=pk)
        serializer = UserPlayListSerializer(playlist)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def put(self, request, pk):
        playlist = get_object_or_404(UserPlayList, pk=pk)
        if request.user == playlist.user:
            serializer = UserPlayListSerializer(playlist, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    @permission_classes([IsAuthenticated])
    def delete(self, request, pk):
        playlist = get_object_or_404(UserPlayList, pk=pk)
        if playlist.user == request.user:
            playlist.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class PlayListSongAPI(APIView):
    @permission_classes([IsAuthenticated])
    def post(self, request, pk):
        from music.models import Song
        playlist = get_object_or_404(UserPlayList, pk=pk)
        if request.user == playlist.user:
            for song_id in request.data["songs"]:
                song = get_object_or_404(Song, id=song_id)
                if not playlist.song.filter(id=song_id).exists():
                    playlist.song.add(song)
            context = {
                'name': playlist.name,
                'song': playlist.song
            }
            serializer = UserPlayListSerializer(playlist, data=context)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


    @permission_classes([IsAuthenticated])
    def delete(self, request, pk):
        from music.models import Song
        playlist = get_object_or_404(UserPlayList, pk=pk)
        print(request.user)
        if request.user == playlist.user:
            for song_id in request.data["songs"]:
                song = get_object_or_404(Song, id=song_id)
                if playlist.song.filter(id=song_id).exists():
                    playlist.song.remove(song)
            context = {
                'name': playlist.name,
                'song': playlist.song
            }
            serializer = UserPlayListSerializer(playlist, data=context)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
