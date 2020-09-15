from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    num = models.CharField(max_length=200, null=True)

class Artist(models.Model):
    # artist_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    debue = models.CharField(max_length=200)
    img = models.URLField(null=True)
    type = models.CharField(max_length=200)
    member = models.CharField(max_length=200, null=True)

class Album(models.Model):
    # album_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    like = models.IntegerField()
    genres = models.ManyToManyField(
        Genre,
        related_name= "album_genres"
    )
    artist = models.ForeignKey(
        Artist,
        related_name="artist_albums",
        on_delete=models.CASCADE
    )
    img = models.URLField(null=True)
    released_date = models.CharField(max_length=200)

class Song(models.Model):
    # song_id = models.IntegerField(primary_key=True)
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
    artist = models.ManyToManyField(
        Artist,
        related_name='artist_songs',
    )
    img = models.URLField(null=True)
    lyric = models.TextField(null=True)
    released = models.CharField(max_length=200)
    type = models.CharField(max_length=200, null=True)