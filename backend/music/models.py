from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, primary_key=True)

class Artist(models.Model):
    artist_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    debut = models.CharField(max_length=200)
    img = models.URLField(null=True)

class Album(models.Model):
    album_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    like = models.IntegerField()
    genre = models.ManyToManyField(
        Genre,
        related_name= "album_genres"
    )
    artist = models.ForeignKey(
        Artist,
        related_name="artist_albums",
        on_delete=models.CASCADE
    )
    intro = models.TextField(null=True)
    img = models.URLField(null=True)

class Song(models.Model):
    song_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    like = models.IntegerField()
    genre = models.ManyToManyField(
        Genre,
        related_name="song_genres"
    )
    album = models.ForeignKey(
        Album,
        related_name='album_songs',
        on_delete=models.CASCADE
    )
    artist = models.ForeignKey(
        Artist,
        related_name='artist_songs',
        on_delete=models.CASCADE
    )
    img = models.URLField(null=True)
    lyric = models.TextField(null=True)
    released = models.CharField(max_length=200)