import os
from pathlib import Path

try:
    from .local_settings import BASE_DIR
except:
    BASE_DIR = Path(__file__).resolve().parent.parent

try:
    from .local_settings import DEBUG
except:
    DEBUG = False

INSTALLED_EXTRA_APPS = [

]

OWN_APPS = [

]

EXTRA_MIDDLEWARE_CLASSES = [
    'django.middleware.locale.LocaleMiddleware',
]

REST_API_VER = 'v1'
REST_API_VERSION = REST_API_VER + '/'

SETTINGS_EXPORT = [
    'DEBUG',
    'PROJECT_NAME',
    'PROJECT_SUB_NAME',
]