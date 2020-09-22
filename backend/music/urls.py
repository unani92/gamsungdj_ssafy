from django.urls import path
from . import views

urlpatterns = [
    path('<str:emotion_type>/', views.SongType.as_view()),
    path('<str:category>/<int:pk>', views.SongDetail.as_view())
]