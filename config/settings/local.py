from .base import *

ALLOWED_HOSTS = ['*',]

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'project',
        'USER': 'root',
        'PASSWORD': 'freefree104460!',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

#python manage.py runserver --settings=config.settings.local
