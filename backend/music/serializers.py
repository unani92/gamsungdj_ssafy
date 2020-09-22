from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Genre, Album, Song, Artist
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
