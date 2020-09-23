from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import settings
from music.models import Song

GENDER_CHOICES = (
        ('M', '남성'),
        ('F', '여성'),
    )
AGE_CHOICES = (
    ('0', '10세 이하'),
    ('1', '10대'),
    ('2', '20대'),
    ('3', '30대'),
    ('4', '40대'),
    ('5', '50대 이상'),
    )


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    avatar = models.ImageField(upload_to='static/image/avatar/', null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    age = models.CharField(max_length=1, choices=AGE_CHOICES, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_signed_up = models.BooleanField(default=False)


class UserPlayList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    song = models.ManyToManyField(Song, related_name="playlist_songs")
    name = models.CharField(max_length=128)