from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Genre, Album, Song, Artist
from accounts.serializers import UserSerializer

class GenreSerializer(serializers.ModelSerializer):
    pass

class ArtistSerializer(serializers.ModelSerializer):
    pass

class AlbumSerializer(serializers.ModelSerializer):
    artist = UserSerializer(many=True)
    class Meta:
        model = Album
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    pass
