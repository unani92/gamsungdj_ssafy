from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Log)
admin.site.register(AlbumComment)
admin.site.register(SongComment)