import os

SITE_ID = 1
DEBUG = True

MEDIA_ROOT = os.path.normcase(os.path.dirname(os.path.abspath(__file__)))
MEDIA_URL = '/media/'

DATABASE_ENGINE = 'sqlite3'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'drf_example',
    }
}

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.auth',
    'django.contrib.admin',
    'rest_framework',
    'example',
    'rest_framework_google_json_style_api',
    'debug_toolbar',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # insert your TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_URL = '/static/'

ROOT_URLCONF = 'example.urls'

SECRET_KEY = 'envive'

MIDDLEWARE = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = ('127.0.0.1', )

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework_google_json_style_api.parsers.JSONParser',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework_google_json_style_api.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
}
