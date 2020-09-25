from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "accounts"
urlpatterns = [
    # social login
    path('google/', views.GoogleLogin.as_view(), name='google_login'),
    path('kakao/', views.KakaoLogin.as_view(), name='kakao_login'),
    # user get, post
    path('', views.UserAPI.as_view()),
    # playlist get, post
    path('playlist/', views.PlaylistAPI.as_view(), name='playlist'),
    # playlist put, delete
    path('playlist/<int:pk>/', views.PlaylistDetailAPI.as_view()),
    # add or delete song in playlist
    path('playlist/<int:pk>/song/<int:song_pk>/', views.PlayListSongAPI.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)