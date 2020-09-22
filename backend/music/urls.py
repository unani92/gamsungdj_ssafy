from django.urls import path
from . import views

urlpatterns = [
    path('search/<str:category>/<str:keyword>/', views.SearchResult.as_view()),
    path('log/', views.CreateLog.as_view()),
    path('<str:emotion_type>/', views.SongType.as_view()),
    path('<str:category>/<int:pk>/', views.CategoryDetail.as_view()),
    path('<str:category>/<int:pk>/like/', views.Like.as_view())
]