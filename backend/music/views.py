from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, APIView
from rest_framework.permissions import IsAuthenticated
from .models import Song, Album, Artist, Log
from .serializers import SongSerializer, AlbumSerializer, ArtistSerializer, LogSerializer

# Create your views here.

class SongType(APIView):
    def get(self, request, emotion_type):
        songs = Song.objects.filter(type__exact=emotion_type).order_by('-like')[:10]
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get(self, request, category, pk):
        if category == 'song':
            song = get_object_or_404(Song, pk=pk)
            serializer = SongSerializer(song)
            return Response(serializer.data)
        elif category == 'album':
            album = get_object_or_404(Album, pk=pk)
            serializer = AlbumSerializer(album)
            return Response(serializer.data)
        elif category == 'artist':
            artist = get_object_or_404(Artist, pk=pk)
            serializer = ArtistSerializer(artist)
            return Response(serializer.data)
        else:
            return Response({
                "status": 401,
                "msg": "invalid approach"
            })

class SearchResult(APIView):
    def get(self, request, category, keyword):
        if category == 'song':
            songs = Song.objects.filter(name__contains=keyword)
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)
        elif category == 'album':
            albums = Album.objects.filter(name__contains=keyword)
            serializer = AlbumSerializer(albums, many=True)
            return Response(serializer.data)
        elif category == 'artist':
            artists = Artist.objects.filter(name__contains=keyword)
            serializer = ArtistSerializer(artists, many=True)
            return Response(serializer.data)
        else:
            return Response({
                "status": 401,
                "msg": "invalid approach"
            })

class CreateLog(APIView):
    @permission_classes([IsAuthenticated])
    def get(self, request):
        logs = Log.objects.filter(user=request.user)
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def post(self, request):
        pk = request.data['song']
        song = get_object_or_404(Song, pk=pk)
        log = Log.objects.create(song=song, user=request.user)
        log.save()
        serializer = LogSerializer(log)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def delete(self, request):
        pk = request.data['id']
        log = get_object_or_404(Log, pk=pk)
        log.delete()
        return Response({'msg': 'deleted'})

class Like(APIView):
    @permission_classes([IsAuthenticated])
    def post(self, request, category, pk):
        user = request.user
        if category == 'song':
            song = get_object_or_404(Song, pk=pk)
            if user in song.user_like.all():
                song.user_like.remove(user)
                liked = False
            else:
                song.user_like.add(user)
                liked = True
            return Response({
                "status": 200,
                "liked": liked
            })
        elif category == 'album':
            album = get_object_or_404(Album, pk=pk)
            if user in album.user_like.all():
                album.user_like.remove(user)
                liked = False
            else:
                album.user_like.add(user)
                liked = True
            return Response({
                "status": 200,
                "liked": liked
            })
        else:
            return Response({
                "status": 400,
                "msg": "잘못된 접근입니다."
            })