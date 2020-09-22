from django.urls import path
from . import views

urlpatterns = [
    path('<str:emotion_type>/', views.SongType.as_view()),
    path('<str:category>/<int:pk>', views.SongDetail.as_view()),
    path('search/<str:category>/<str:keyword>/', views.SearchResult.as_view()),
    path('create/log/', views.CreateLog.as_view())
]