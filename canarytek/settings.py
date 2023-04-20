"""
Django settings for canarytek project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#oe=epr#z*u+&!xqd2)klwwp8q9i@&)s07urh@#!805sn*bynb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['myapi.canarytek.es', '127.0.0.1']

AUTHENTICATION_BACKENDS = [    
    'myapp.custom_saml_auth_backend.CustomSAMLAuthBackend',

]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_saml2_auth',
    'sslserver',
    'djangosaml2'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]




ROOT_URLCONF = 'canarytek.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            '/home/canarytek1/Escritorio/canarytek/myapp/templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'canarytek.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




SAML2_AUTH = {

    'DEFAULT_NEXT_URL': '/home/',
    'ENTITY_ID': 'https://id.modularit.net',
    'NAME_ID_FORMAT': 'urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified',
    'USE_JWT': False,
    'ASSERTION_URL': 'https://myapi.canarytek.es:8000',
    'METADATA_LOCAL_FILE_PATH': '/home/canarytek1/Escritorio/canarytek/metadata.xml',
    #'METADATA_AUTO_CONF_URL': 'https://id.modularit.net/api/v3/providers/saml/8/metadata/',

    'CREATE_USER': True, # Create a new Django user when a new user logs in. Defaults to True.
    'NEW_USER_PROFILE': {
        'USER_GROUPS': [],  # The default group name when a new user logs in
        'ACTIVE_STATUS': True,  # The default active status for new users
        'STAFF_STATUS': True,  # The staff status for new users
        'SUPERUSER_STATUS': True,  # The superuser status for new users
        
    },  
    'ATTRIBUTES_MAP': {  # Change Email/UserName/FirstName/LastName to corresponding SAML2 userprofile attributes.
        'email': 'emailAddress',
        'username': 'name',
        'first_name': 'name',
        'last_name': 'http://schemas.goauthentik.io/2021/02/saml/uid',
    },
}

#ver el atributo que mapea
# permisos por grupo
# cuando cree un usuario que lo cree con los permisos de el grupo




LOGIN_URL = 'saml2_auth_login'


# import logging

# # Configure logging
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s %(levelname)s %(message)s',
#     filename='debug.log',
#     filemode='a'
# )


# import logging

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
#         },
#     },
# }



