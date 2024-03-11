from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'user'

urlpatterns = [
    path('', views.index, name='index'),
    path('verification/', views.verification, name='verification'),
    path('api/get-users/', views.get_users, name='get_users'),
    path('api/get-verification/', views.get_verification, name='get_users_verify')
]