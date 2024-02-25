from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'social_trading'

urlpatterns = [
    path('', views.index, name='index'),
    path('subscription/', views.subscription, name='subscription'),
    path('fee/', views.fee, name='fee'),
    path('master_fee/', views.master_fee, name='master_fee'),
    path('configuration/', views.configuration, name='configuration'),
]