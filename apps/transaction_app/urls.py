from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'transaction'

urlpatterns = [
    path('', views.index, name='index'),
    path('withdrawal/', views.withdrawal, name='withdrawal'),
    path('internal_trans/', views.internal_trans, name='internal_trans'),
]