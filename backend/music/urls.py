from django.urls import path
from . import views, recommend

urlpatterns = [
    path('addsrc/<int:pk>/', views.AddYoutubeId.as_view()),
    path('search/<str:category>/<str:keyword>/', views.SearchResult.as_view()),
    path('log/', views.CreateLog.as_view()),
    path('album/<int:pk>/comment/', views.AlbumCommentList.as_view()),
    path('song/<int:pk>/comment/', views.SongCommentList.as_view()),
    path('musicdna/<str:category>/', views.MusicDna.as_view()),
    path('<str:emotion_type>/', views.SongType.as_view()),
    path('<str:category>/<int:pk>/', views.CategoryDetail.as_view()),
    path('<str:category>/<int:pk>/like/', views.Like.as_view()),
    path('recommend/time/', recommend.TimeRecommend.as_view()),
]
