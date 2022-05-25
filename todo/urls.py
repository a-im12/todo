from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('mypage', views.IndexViews.as_view(), name='mypage.html')
]