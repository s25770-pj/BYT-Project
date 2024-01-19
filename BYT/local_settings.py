import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

##########################################################
# Basic flags / parameters
##########################################################

MEDIA_ROOT = os.path.join(BASE_DIR, '_media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, '_static')
STATIC_URL = '/static/'
CONFIG_ALLOWED_HOSTS = [
    '127.0.0.1',
    '57.128.197.32',
    'localhost',
    '*',
]
MAX_UPLOAD_SIZE = 104785760

##########################################################
# DATABASES
##########################################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

##########################################################
# CORS HEADERS
##########################################################

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8088',
    'http://localhost:8008',
    'http://127.0.0.1:8088',
    'http://127.0.0.1:8008',
]
