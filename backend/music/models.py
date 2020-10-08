from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=300, primary_key=True)
    num = models.CharField(max_length=300, null=True)

class Artist(models.Model):
    # artist_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    debue = models.CharField(max_length=300)
    img = models.URLField(null=True)
    type = models.CharField(max_length=300)
    member = models.CharField(max_length=300, null=True)

class Album(models.Model):
    # album_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    like = models.IntegerField()
    genres = models.ManyToManyField(
        Genre,
        related_name= "album_genres"
    )
    artist = models.ManyToManyField(
        Artist,
        related_name="artist_albums",
    )
    user_like = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_albums',
    )
    img = models.URLField(null=True)
    released_date = models.CharField(max_length=300)
    songs = models.TextField(null=True)

class Song(models.Model):
    # song_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    like = models.IntegerField()
    genres = models.ManyToManyField(
        Genre,
        related_name="song_genres"
    )
    album = models.ForeignKey(
        Album,
        related_name='album_songs',
        on_delete=models.CASCADE
    )
    user_like = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_songs',
    )
    artist = models.ManyToManyField(
        Artist,
        related_name='artist_songs',
    )
    img = models.URLField(null=True)
    lyric = models.TextField(null=True)
    released = models.CharField(max_length=300)
    src = models.CharField(max_length=300, null=True, default='')
    type = models.CharField(max_length=300, null=True)

class Log(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_logs',
        on_delete=models.CASCADE
    )
    song = models.ForeignKey(
        Song,
        related_name='song_logs',
        on_delete=models.CASCADE
    )
    time = models.DateTimeField(auto_now_add=True)

class AlbumComment(models.Model):
    album = models.ForeignKey(
        Album,
        related_name='comment_albums',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_album_comments',
        on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SongComment(models.Model):
    song = models.ForeignKey(
        Song,
        related_name='comment_songs',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_song_comments',
        on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)