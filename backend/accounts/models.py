from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import settings
from music.models import Song

class User(AbstractUser):
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
    avatar = models.ImageField(upload_to='static/image/avatar/', null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='F')
    age = models.CharField(max_length=1, choices=AGE_CHOICES, default='2')


class UserPlayList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    song = models.ManyToManyField(Song)
    name = models.CharField(max_length=128)