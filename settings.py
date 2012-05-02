import os, sys

DIRNAME = os.path.dirname(__file__)

DEBUG = True

DATABASES = {'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(DIRNAME, 'database.db'),
    },
}

ROOT_URLCONF = 'apptemplate.tests.urls'

INSTALLED_APPS = (
    #'django.contrib.auth',
    #'django.contrib.sessions',
    'apptemplate',
)

SECRET_KEY = 'temporary-test-key'
