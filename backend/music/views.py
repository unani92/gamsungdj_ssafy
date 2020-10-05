from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, APIView
from rest_framework.permissions import IsAuthenticated
from .models import Song, Album, Artist, Log, AlbumComment, SongComment, Genre
from .serializers import SongSerializer, AlbumSerializer, ArtistSerializer, LogSerializer, AlbumCommentSerializer, SongCommentSerializer
from random import sample
import re
# Create your views here.

class SongType(APIView):
    def get(self, request, emotion_type):
        songs = Song.objects.filter(type__exact=emotion_type).order_by('-like')[:200]
        selected = list(sample(range(0,200), 10))
        songs = [songs[i] for i in selected]
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
            songs = Song.objects.filter(album=pk)

            serializer = AlbumSerializer(album)
            song_serializer = SongSerializer(songs, many=True)
            return Response({
                "data": serializer.data,
                "songs": song_serializer.data
            })
        elif category == 'artist':
            artist = get_object_or_404(Artist, pk=pk)
            serializer = ArtistSerializer(artist)
            songs = Song.objects.filter(artist=pk)
            song_serializer = SongSerializer(songs, many=True)
            albums = Album.objects.filter(artist=pk)
            album_serializer = AlbumSerializer(albums, many=True)
            return Response({
                'data': serializer.data,
                'songs': song_serializer.data,
                'albums': album_serializer.data
            })
        else:
            return Response({
                "status": 401,
                "msg": "invalid approach"
            })

class SearchResult(APIView):
    def get(self, request, category, keyword):
        if category == 'song':
            songs = Song.objects.filter(name__contains=keyword).order_by('-pk')
            try:
                artist = Artist.objects.get(name__contains=keyword)
                artist_songs = Song.objects.filter(artist=artist.pk)
            except:
                artist_songs = []

            songs = list(artist_songs) + list(songs)
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)
        elif category == 'album':
            albums = Album.objects.filter(name__contains=keyword).order_by('-pk')
            serializer = AlbumSerializer(albums, many=True)
            return Response(serializer.data)
        elif category == 'artist':
            artists = Artist.objects.filter(name__contains=keyword).order_by('-pk')
            serializer = ArtistSerializer(artists, many=True)
            return Response(serializer.data)
        else:
            return Response({
                "status": 401,
                "msg": "invalid approach"
            })

class MusicDna(APIView):
    @permission_classes([IsAuthenticated])
    def get(self, request, category):
        print(request.GET)
        emotion = request.GET['emotion']
        keyword = request.GET['keyword']
        if category == 'artist':
            artist = Artist.objects.get(name__contains=keyword)
            songs = Song.objects.filter(artist=artist.pk, type=emotion)\
                .exclude(like__lt=500)
            if len(songs) >= 10:
                nums = sample(range(len(songs)),10)
            else:
                nums = range(len(songs))
            songs = [songs[i] for i in nums]
            serializer = SongSerializer(songs, many=True)
        elif category == 'genre':
            genre = Genre.objects.get(name__contains=keyword)
            songs = Song.objects.filter(genres__in=[genre], type=emotion)\
                .exclude(like__lt=500)

            if len(songs) >= 20:
                nums = sample(range(len(songs)), 20)
            else:
                nums = range(len(songs))
            songs = [songs[i] for i in nums]
            serializer = SongSerializer(songs, many=True)
        else:
            return Response({'msg': 'failed'})

        return Response(serializer.data)

class CreateLog(APIView):
    @permission_classes([IsAuthenticated])
    def get(self, request):
        logs = Log.objects.filter(user=request.user).exclude(song__type='no lyric')
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
        print(user)
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

class AlbumCommentList(APIView):
    def get(self, request, pk):
        album = get_object_or_404(Album, pk=pk)
        comments = AlbumComment.objects.filter(album=album)
        song_comments = SongComment.objects.filter(song__album=pk)

        song_serializer = SongCommentSerializer(song_comments, many=True)
        serializer = AlbumCommentSerializer(comments, many=True)
        return Response({
            'albumComment': serializer.data,
            'songComment': song_serializer.data
        })

    @permission_classes([IsAuthenticated])
    def post(self, request, pk):
        album = get_object_or_404(Album, pk=pk)
        serializer = AlbumCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, album=album)
            return Response(serializer.data)
        else:
            return Response({"msg": 'error'})

    @permission_classes([IsAuthenticated])
    def put(self, request, pk):
        comment = get_object_or_404(AlbumComment, pk=pk)
        if request.user.username == comment.user.username:
            serializer = AlbumCommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({
                    "status": 200,
                    "data": serializer.data
                })
            else:
                return Response({
                    "status": 500,
                    "msg": "댓글 수정에 실패했습니다."
                })
        else:
            return Response({
                "status": 401,
                "msg": "게시글 수정 권한이 없습니다."
            })

    @permission_classes([IsAuthenticated])
    def delete(self, request, pk):
        comment = get_object_or_404(AlbumComment, pk=pk)
        if request.user.username == comment.user.username:
            comment.delete()
            return Response({
                "status": 200,
                "msg": "deleted"
            })
        else:
            return Response({
                "status": 401,
                "msg": "게시글 삭제 권한이 없습니다."
            })

class SongCommentList(APIView):
    def get(self, request, pk):
        song = get_object_or_404(Song, pk=pk)
        comments = SongComment.objects.filter(song=song)
        serializer = SongCommentSerializer(comments, many=True)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def post(self, request, pk):
        song = get_object_or_404(Song, pk=pk)
        serializer = SongCommentSerializer(data=request.data)
        print(request.user)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, song=song)
            return Response(serializer.data)
        else:
            return Response({"msg": 'error'})

    @permission_classes([IsAuthenticated])
    def put(self, request, pk):
        comment = get_object_or_404(SongComment, pk=pk)
        if request.user.username == comment.user.username:
            serializer = SongCommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({
                    "status": 200,
                    "data": serializer.data
                })
            else:
                return Response({
                    "status": 500,
                    "msg": "댓글 수정에 실패했습니다."
                })
        else:
            return Response({
                "status": 401,
                "msg": "게시글 수정 권한이 없습니다."
            })

    @permission_classes([IsAuthenticated])
    def delete(self, request, pk):
        comment = get_object_or_404(SongComment, pk=pk)
        if request.user.username == comment.user.username:
            comment.delete()
            return Response({
                "status": 200,
                "msg": "deleted"
            })
        else:
            return Response({
                "status": 401,
                "msg": "게시글 삭제 권한이 없습니다."
            })

class AddYoutubeId(APIView):
    def post(self, request, pk):
        song = get_object_or_404(Song, pk=pk)
        src = request.data['src']
        if not song.src:
            song.src = src
            song.save()
            serializer = SongSerializer(song)
            return Response(serializer.data)
        else:
            return Response({
                'msg': 'failed'
            })