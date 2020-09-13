from django.contrib.auth.models import AbstractUser
# from django.db import models


class User(AbstractUser):
    pass
    # email = models.EmailField(max_length=255, unique=True)
    # nickname = models.CharField(
    #     max_length=10,
    #     blank=False,
    #     unique=True,
    #     default='')
    # avatar = models.ImageField(
    #     null=True,
    #     blank=True,
    #     upload_to='image/avatar/',
    # )
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['nickname']