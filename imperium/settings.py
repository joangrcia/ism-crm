from django.utils.translation import gettext_lazy as _
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6hx(%3hxb&5*-)6n+8p_19z2s4kl6gf^rbrn!07&c(a94jkc&m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tailwind',
    'theme',
    "phonenumber_field",
    'apps.dashboard_app',
    'apps.user_app',
    'apps.trading_account_app',
    'apps.partner_app',
    'apps.social_trading_app',
    'apps.transaction_app',
    'apps.notice_app',
    'apps.product_app',
    # 2fa
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'two_factor',
    'dynamic_breadcrumbs',
    'fast_pagination',
    # htmx
    'django_htmx',
    'debug_toolbar',
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    "django_htmx.middleware.HtmxMiddleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'strip_whitespace.middlewares.HtmlStripWhiteSpaceMiddleware.html_strip_whitespace',
]

ROOT_URLCONF = 'imperium.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "dynamic_breadcrumbs.context_processors.breadcrumbs",
            ],
        },
    },
]

WSGI_APPLICATION = 'imperium.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'railway',
        'USER': 'dbadmin',
        'PASSWORD': 'Mars012023',
        'HOST': '128.199.127.203',
        'PORT': '5432',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'railway',
#         'USER': 'postgres',
#         'PASSWORD': 'Mars012023',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://localhost:6379",  # Sesuaikan dengan konfigurasi Redis Anda
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }

# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = "default"

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Untuk mengumpulkan file-file statis
MEDIA_URL = '/media/'  # URL yang digunakan untuk mengakses file media
# Menyimpan file-file media seperti gambar
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LOGIN_URL = 'login'  # Ganti dengan URL halaman login kustom Anda
# LOGIN_REDIRECT_URL = 'login'  # Ganti dengan URL halaman login kustom Anda
# LOGOUT_REDIRECT_URL = 'login'  # Ganti dengan URL halaman login kustom Anda

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]
NPM_BIN_PATH = 'npm.cmd'


LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
    ('id', _('Indonesia')),
    ('de', _('German')),
    ('it', _('Italian')),
    ('ja', _('Japanese')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)

LOGIN_URL = 'login'

LOGIN_REDIRECT_URL = 'dashboard:index'
