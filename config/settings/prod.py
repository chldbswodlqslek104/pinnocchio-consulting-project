from .base import *

ALLOWED_HOSTS = ['choiyunjae.pythonanywhere.com', '127.0.0.1' ,]


DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'choiyunjae$project',
        'USER': 'choiyunjae',
        'PASSWORD': 'teampw220207!!',
        'HOST': 'choiyunjae.mysql.pythonanywhere-services.com',
    }
}

#python manage.py runserver --settings=config.settings.prod