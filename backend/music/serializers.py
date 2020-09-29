from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Genre, Album, Song, Artist, Log, AlbumComment, SongComment
from accounts.serializers import UserSerializer

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=True)
    genres = GenreSerializer(many=True)
    user_like = UserSerializer(many=True)

    class Meta:
        model = Album
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    album = AlbumSerializer()
    artist = ArtistSerializer(many=True)
    user_like = UserSerializer(many=True)

    class Meta:
        model = Song
        fields = '__all__'

class LogSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    song = SongSerializer()
    class Meta:
        model = Log
        fields = '__all__'

class AlbumCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    album = AlbumSerializer(required=False)
    class Meta:
        model = AlbumComment
        fields = ['pk','user', 'album', 'content', 'updated_at']

class SongCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    song = SongSerializer(required=False)
    class Meta:
        model = SongComment
        fields = ['pk','user', 'song', 'content', 'updated_at']

