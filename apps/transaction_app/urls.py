from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'transaction'

urlpatterns = [
    path('', views.index, name='index'),
    path('get/', views.deposit_get, name='deposit_get'),
    path('get-history/', views.deposit_history_get, name='deposit_history_get'),
    path('update/', views.deposit_update, name='deposit_update'),
    path('delete/', views.deposit_delete, name='deposit_delete'),
    path('withdrawal/', views.withdrawal, name='withdrawal'),
    path('withdrawal/get/', views.withdrawal_get, name='withdrawal_get'),
    path('withdrawal/get-history/', views.withdrawal_history_get, name='withdrawal_history_get'),
    path('withdrawal/update/', views.withdrawal_update, name='withdrawal_update'),
    path('withdrawal/delete/', views.withdrawal_delete, name='withdrawal_delete'),
    path('internal_trans/', views.internal_trans, name='internal_trans'),
    path('internal_trans/get/', views.internal_trans_get, name='internal_trans_get'),
    path('internal_trans/get-history/', views.internal_trans_history_get, name='internal_trans_history_get'),
    path('internal_trans/update/', views.internal_trans_update, name='internal_trans_update'),
    path('internal_trans/delete/', views.internal_trans_delete, name='internal_trans_delete'),
]