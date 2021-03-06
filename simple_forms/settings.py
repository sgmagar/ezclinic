"""
Django settings for simple_forms project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from djangae.settings_base import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(_x%ddeemso%6ur5@d_z*ngdd3=yu0x4v^5#l4##7f2gwm7nhu'

# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'core.User'
AUTHENTICATION_BACKENDS = ['simple_forms.apps.core.auth.EmailOrUsernameModelBackend']
LOGIN_URL = 'login_user'


GENERATE_SPECIAL_INDEXES_DURING_TESTING = True

# Application definition

INSTALLED_APPS = [
    'djangae',
    'djangae.contrib.security',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangae.contrib.contenttypes',
    'widget_tweaks',
    'django.contrib.admin',
    'simple_forms.apps.core',
]

EMAIL_BACKEND = 'djangae.mail.EmailBackend'
# Uncomment to show email body in console
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'djangae.contrib.security.middleware.AppEngineSecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'djangae.contrib.security.middleware.AppEngineSecurityMiddleware',
]

ROOT_URLCONF = 'simple_forms.urls'

STATIC_ROOT = '/apps/core/static/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'simple_forms/templates')],
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

WSGI_APPLICATION = 'simple_forms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

import os
DATABASES = {
    'default': {
        'ENGINE': 'djangae.db.backends.appengine'
    }}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

BUCKET_KEY='ezclinic-dental.appspot.com'



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'


#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = ''
MEDIA_URL = '/media/'
