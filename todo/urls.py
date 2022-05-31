from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('mypage/', views.MypageViews.as_view(), name='mypage'),
    path('post/', views.CreatePostView.as_view(), name='post'),
    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),
]