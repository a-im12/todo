from django.urls import path
from django import views as auth_view
from . import views

app_name='acounts'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signup_success/', views.SignupSuccessView.as_view(), name='signup_success')
]