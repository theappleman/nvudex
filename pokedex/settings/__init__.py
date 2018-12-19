"""
Django settings for pokedex project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys
import string
from random import SystemRandom

from django.core.exceptions import ImproperlyConfigured
from djangae.settings_base import *


def env(env_var):
    try:
        return os.environ[env_var]
    except KeyError:
        error_msg = "Set the {} environment variable".format(env_var)
    raise ImproperlyConfigured(error_msg)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
try:
    SECRET_KEY = env("SECRET_KEY")
except ImproperlyConfigured:
    SECRET_FILE = os.path.join(BASE_DIR, 'secretkey.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            SECRET_KEY = ''.join([SystemRandom().choice("".join([string.ascii_letters, string.digits, string.punctuation])) for i in range(63)])
            with open(SECRET_FILE, 'w') as secret:
                secret.write(SECRET_KEY)
        except IOError:
            raise ImproperlyConfigured('Please create the {} file with random characters \
                    to generate your secret key!'.format(SECRET_FILE))

# By default, run with DEBUG=False
# Debug environments must re-enable debug mode
# An empty string is bool(False)
os.environ.setdefault("DEBUG", "")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(env("DEBUG"))

try:
    ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")
except:
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
    sys.stderr.write("No ALLOWED_HOSTS provided; defaulting to: {}\n".format(", ".join(ALLOWED_HOSTS)))

# Detect proxied SSL header
# https://docs.djangoproject.com/en/1.11/ref/settings/#secure-proxy-ssl-header
os.environ.setdefault("SSL", "")
ssl = bool(env("SSL"))
if ssl:
    sys.stderr.write("Enabling SSL proxy header\n")
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
else:
    sys.stderr.write("Not enabling SSL proxy header\n")

# Application definition

INSTALLED_APPS = [
        'djangae',
        'django.contrib.auth',
        'djangae.contrib.gauth_datastore',
        'django.contrib.contenttypes',
        'djangae.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'djangae.contrib.security',
        'elements.apps.ElementsConfig',
        'species.apps.SpeciesConfig',
]

MIDDLEWARE = [
        'djangae.contrib.security.middleware.AppEngineSecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'djangae.contrib.gauth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'session_csrf.CsrfMiddleware',
]

ROOT_URLCONF = 'pokedex.urls'

TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
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

WSGI_APPLICATION = 'pokedex.wsgi.application'
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
        'default': {
            'ENGINE': 'djangae.db.backends.appengine',
        }
}
# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

AUTH_USER_MODEL = "gauth_datastore.GaeDatastoreUser"
AUTHENTICATION_BACKENDS = (
    'djangae.contrib.gauth_datastore.backends.AppEngineUserAPIBackend',
)
