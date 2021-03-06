from base import *


############################################################
##### DATABASE #############################################
############################################################

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}',
        'USER': '{{ project_name }}',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


############################################################
##### OTHER ################################################
############################################################

DEBUG = True
TEMPLATE_DEBUG = True