import os
SECRET_KEY = 'test'
INSTALL_DIR = '/usr/local/dynamic-rest/'
STATIC_URL = '/static/'
STATIC_ROOT = INSTALL_DIR + 'www/static'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': INSTALL_DIR + 'db.sqlite3',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''
    }
}

MIDDLEWARE_CLASSES = ()

INSTALLED_APPS = (
    'rest_framework',
    'django.contrib.staticfiles',
    'tests',
)

REST_FRAMEWORK = {
    'PAGE_SIZE': 50,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'dynamic_rest.renderers.DynamicBrowsableAPIRenderer'
    )
}
ROOT_URLCONF = 'tests.urls'

BASE_DIR = os.path.dirname(__file__)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, '../dynamic_rest/templates'),
)

DYNAMIC_REST = {
    'ENABLE_LINKS': True,
    'DEBUG': os.environ.get('DYNAMIC_REST_DEBUG', 'false').lower() == 'true'
}
