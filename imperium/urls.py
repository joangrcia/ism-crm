from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from . import views

urlpatterns = i18n_patterns (
    path('admin/', admin.site.urls, name='adminpage'),
    path('', views.index, name='login'),
    path('dashboard/', include('apps.dashboard_app.urls')),
)