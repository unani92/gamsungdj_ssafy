from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, APIView
from rest_framework.permissions import IsAuthenticated
from .models import Song, Album, Artist, Log, AlbumComment, SongComment
from .serializers import SongSerializer, AlbumSerializer, ArtistSerializer, LogSerializer, AlbumCommentSerializer, SongCommentSerializer
from random import sample
from datetime import datetime
from collections import Counter
import math
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
            songs = [song for song in album.songs.split(',')]
            print(songs)
            artist = album.artist.name
            arr = []
            for idx,song in enumerate(songs):
                try:
                    s = Song.objects.filter(name__exact=song, album=album)[0]
                    serializer = SongSerializer(s)
                    arr.append(serializer.data)
                except:
                    arr.append('')

            serializer = AlbumSerializer(album)
            return Response({
                "data": serializer.data,
                "songs": arr
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

class TimeRecommend(APIView):
    def get(self, request):
        now = datetime.now()
        hour = now.hour

        if request.user.is_authenticated:  # logged in user
            recommend = []

            # 사용자가 좋아요를 누른 곡은 추천에서 제외
            sad_songs_all = Song.objects.filter(type__exact='sad').exclude(user_like__in=[request.user]).order_by('-like')
            love_songs_all = Song.objects.filter(type__exact='love').exclude(user_like__in=[request.user.pk]).order_by('-like')
            joy_songs_all = Song.objects.filter(type__exact='joy').exclude(user_like__in=[request.user.pk]).order_by('-like')

            # extract all user's logs by time
            if 0<= hour < 7:
                logs = Log.objects.filter(user=request.user, time__hour__range=(0,7))
            elif 7<= hour < 11:
                logs = Log.objects.filter(user=request.user, time__hour__range=(7,11))
            elif 12 <= hour < 14:
                logs = Log.objects.filter(user=request.user, time__hour__range=(12,14))
            elif 20 <= hour <= 23:
                logs = Log.objects.filter(user=request.user, time__hour__range=(20,24))
            else:
                logs = Log.objects.filter(user=request.user)

            # log based recommend
            if logs:
                feelings = [log.song.type for log in logs]
                counts = {'sad': 0, 'joy': 0, 'love': 0}
                for feel in feelings:
                    counts[feel] += 1
                sad_prop = int(counts['sad'] / len(feelings)*100)
                joy_prop = int(counts['joy'] / len(feelings) * 100)
                love_prop = int(counts['love'] / len(feelings) * 100)

                sad_songs = math.ceil(sad_prop/100 * 12)
                joy_songs = math.ceil(joy_prop/100 * 12)
                love_songs = math.ceil(love_prop/100 * 12)

            else:    # if user's log not exist
                pass

            return Response({
                'status': 200
            })


        else:    # not logged in
            return Response({
                'data': 'noooooooooo'
            })