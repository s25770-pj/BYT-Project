from pathlib import Path
import os

SECRET_KEY = 'django-insecure-yza7qxc@j!+_ujf@^_vf2*y!4wwu_)yswq(aso5r&o#rowl-!s'

from .local_settings import *
from .modules_settings import *

if DEBUG:
    ALLOWED_HOSTS = [
        '*'
    ]
else:
    if CONFIG_ALLOWED_HOSTS:
        ALLOWED_HOSTS = CONFIG_ALLOWED_HOSTS
    else:
        ALLOWED_HOSTS = [
            'localhost',
            '127.0.0.1',
        ]

try:
    MEDIA_ROOT
except:
    MEDIA_ROOT = os.path.join(BASE_DIR, '_media')

try:
    MEDIA_URL
except:
    MEDIA_URL = '/media/'

try:
    STATIC_ROOT
except:
    STATIC_ROOT = os.path.join(BASE_DIR, '_static')

try:
    STATIC_URL
except:
    STATIC_URL = os.path.join(BASE_DIR, '/static/')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

if INSTALLED_EXTRA_APPS:
    INSTALLED_APPS += INSTALLED_EXTRA_APPS

if OWN_APPS:
    INSTALLED_APPS += OWN_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BYT.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'BYT.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'pl'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
