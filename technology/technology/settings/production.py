from technology.settings.basesettings import *
import os

SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_PROD_USER'],
        'PASSWORD': os.environ['DATABASE_PROD_PWD'],
        'HOST': os.environ['DATABASE_PROD_HOST'],
        'PORT': os.environ['DATABASE_PORT'],
        'OPTIONS': {
            'init_command': "SET sql_mode = 'STRICT_TRANS_TABLES'"
        }
    }
}


