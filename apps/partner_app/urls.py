from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'partner'

urlpatterns = [
    path('', views.index, name='index'),
    path('wallet/', views.wallet, name='wallet'),
    path('verification/', views.verification, name='verification'),
    path('request/', views.request, name='request'),
]