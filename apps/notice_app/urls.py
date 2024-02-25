from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'notice'

urlpatterns = [
    path('', views.index, name='index'),
]