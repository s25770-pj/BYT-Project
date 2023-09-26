from pathlib import Path

try:
    from .local_settings import BASE_DIR
except:
    BASE_DIR = Path(__file__).resolve().parent.parent

try:
    from .local_settings import DEBUG
except Exception as e:
    DEBUG = False

##############################################################
# DJANGO'S GENERAL BASE_DIR, MEDIA AND STATIC FILES SETTINGS
##############################################################

INSTALLED_EXTRA_APPS = [
]

OWN_APPS = [

]

EXTRA_MIDDLEWARE_CLASSES = [
    'django.middleware.locale.LocaleMiddleware',
]

if DEBUG:
    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ),
        'DEFAULT_PARSER_CLASSES': (
            'rest_framework.parsers.JSONParser',
        ),
        'DEFAULT_PERMISSION_CLASSES': (

        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.TokenAuthentication',
        ),
        'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE': 50,
        'COMPACT_JSON': True,
    }
else:
    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
        ),
        'DEFAULT_PARSER_CLASSES': (
            'rest_framework.parsers.JSONParser',
        ),
        'DEFAULT_PERMISSION_CLASSES': (

        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.TokenAuthentication',
        ),
        'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE': 50,
        'COMPACT_JSON': True,
    }

REST_API_VER = 'v1'
REST_API_VERSION = REST_API_VER + '/'

##############################################################
# DJANGO SETTINGS EXPORT
##############################################################

SETTINGS_EXPORT = [
    'DEBUG',
    'PROJECT_NAME',
    'PROJECT_SUB_NAME',
    'SHOW_AUTHENTICATED_USER',
]

