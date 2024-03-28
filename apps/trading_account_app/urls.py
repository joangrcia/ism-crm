from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'trading'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/trading-account', views.get_taccount, name='api'),
]