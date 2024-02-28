from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from two_factor.urls import urlpatterns as tf_urls

from . import views

urlpatterns = i18n_patterns (
    path('admin/', admin.site.urls, name='adminpage'),
    path('', views.index, name='login'),
    path('send_email', views.send_email, name='send_email'),
    path('dashboard/', include('apps.dashboard_app.urls')),
    path('member/', include('apps.user_app.urls')),
    path('partner/', include('apps.partner_app.urls')),
    path('match-account/', include('apps.match_account_app.urls')),
    path('transaction/', include('apps.transaction_app.urls')),
    path('social-trading/', include('apps.social_trading_app.urls')),
    path('notice/', include('apps.notice_app.urls')),
    path('', include(tf_urls)),
)