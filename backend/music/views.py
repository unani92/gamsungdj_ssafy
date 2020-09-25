from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, APIView
from rest_framework.permissions import IsAuthenticated
from .models import Song, Album, Artist, Log, AlbumComment, SongComment
from .serializers import SongSerializer, AlbumSerializer, ArtistSerializer, LogSerializer, AlbumCommentSerializer, SongCommentSerializer
from random import sample
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
            return Response(serializer.data)
        else:
            return Response({
                "status": 401,
                "msg": "invalid approach"
            })

class SearchResult(APIView):
    def get(self, request, category, keyword):
        if category == 'song':
            songs = Song.objects.filter(name__contains=keyword).order_by('-pk')
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
        serializer = AlbumCommentSerializer(comments, many=True)
        return Response(serializer.data)

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