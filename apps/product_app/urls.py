from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='index'),
    path('checker/', views.checker, name='checker'),
    path('get/', views.get, name='get'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
]