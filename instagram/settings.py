import os
import dj_database_url
import django_heroku
from decouple import config, Csv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Email configurations
EMAIL_USE_TLS = config('EMAIL_USE_TLS')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# Application definition
WSGI_APPLICATION = 'instagram.wsgi.application'
LOGIN_REDIRECT_URL = '/home'

if config('MODE')=="dev":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DBNAME'),
            'USER': config('DBUSER'),
            'PASSWORD': config('DBPASS')
        }
    }
# production
else:
   DATABASES = {
       'default': dj_database_url.config(
           default=config('DATABASE_URL')
       )
   }

INSTALLED_APPS = [
    'app',
    'pyuploadcare.dj',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce',
    'bootstrap4',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'instagram.urls'

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
                'django.template.context_processors.media',
            ],
        },
    },
]

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_L10N = True
USE_TZ = True

db_from_env=dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATICFILES_STORAGE='whitenoise.django.GzipManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

MODE=config("MODE", default="dev")
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = ['*']

UPLOADCARE = {
    'pub_key': config('pub_key'),
    'secret': config('secret'),
}
django_heroku.settings(locals())
