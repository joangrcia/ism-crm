from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'partner'

urlpatterns = [
    path('', views.index, name='index'),
    path('get/', views.partner_get, name='partner_get'),
    path('update/', views.partner_update, name='partner_update'),
    path('wallet/', views.wallet, name='wallet'),
    path('history/get/', views.history_get, name='history_get'),
    path('verification/', views.verification, name='verification'),
    path('verification/get/', views.verify_get, name='verify_get'),
    path('verification/update/', views.verify_update, name='verify_update'),
    path('verification/delete/', views.verify_delete, name='verify_delete'),
    path('request/', views.request, name='request'),
]