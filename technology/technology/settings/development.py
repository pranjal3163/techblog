from technology.settings.basesettings import *

import os

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_LOCAL_USER'],
        'PASSWORD': os.environ['DATABASE_LOCAL_PWD'],
        'HOST': os.environ['DATABASE_LOCAL_HOST'],
        'PORT': os.environ['DATABASE_PORT'],
        'OPTIONS': {
            'init_command': "SET sql_mode = 'STRICT_TRANS_TABLES'"
        }
    }
}


