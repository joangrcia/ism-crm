from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='adminpage'),
    path('', views.index, name='login'),
    path('dashboard/', include('apps.dashboard_app.urls')),

]