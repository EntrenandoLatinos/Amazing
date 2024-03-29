"""
Django settings for amazing project.
Generated by 'django-admin startproject' using Django 3.2.13.
"""

import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# Email definition
EMAIL_USE_SSL = config('EMAIL_USE_SSL', cast=bool)
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT')

# Application definition
BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_APSS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'ckeditor',
]

LOCAL_APPS = [
    'app_core',
    'app_user',
]

INSTALLED_APPS = BASE_APPS + THIRD_APSS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
]

CKEDITOR_CONFIGS = {
    'comment_ckeditor': {
        'toolbar': 'custom',
        'toolbar_custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ["TextColor", "BGColor", 'RemoveFormat'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink'],
            ["Smiley", "SpecialChar", 'Blockquote'],
        ],
        'extraPlugins': 'codesnippet',
        'width': 'auto',
        'height': '180',
        'tabSpaces': 4,
        'removePlugins': 'elementspath',
        'resize_enabled': False,
    },

    'default': {
        'skin': 'office2013',
        'toolbar': 'full',
        'height': 420,
        'width': 'auto',
        'extraPlugins': 'codesnippet',
        "versionCheck": False,
    },
}

ROOT_URLCONF = 'amazing.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'amazing.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env/')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1
ACCOUNT_EMAIL_SUBJECT_PREFIX = '¡Amazing Roofing Team! - '
LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = 'app_user:login-redirect'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
# ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_RATE_LIMITS = {
    'login_failed': {'limit': 6, 'timeout': 300},  # 6 intentos de inicio de sesión fallidos en 5 minutos
}
ACCOUNT_USERNAME_MIN_LENGTH = 4
# ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True

FILE_UPLOAD_PERMISSIONS = 0o644