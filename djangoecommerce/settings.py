
import os
from decouple import config
from dj_database_url import parse as dburl


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'catalog',
    'widget_tweaks',
    'accounts',
    'checkout',
    'paypal.standard.ipn',
    'easy_thumbnails',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'checkout.middleware.cart_item_middleware',
]

ROOT_URLCONF = 'djangoecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #apps
                'catalog.context_processors.categories',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoecommerce.wsgi.application'

default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = { 'default': config('DATABASE_URL', default=default_dburl, cast=dburl), }

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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#auth
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'index'
LOGOUT_URL = 'accounts:logout'
LOGOUT_REDIRECT_URL = 'index'

#aws
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'

AWS_S3_SECURE_URLS = True
AWS_QUERYSTRING_AUTH = False
AWS_PRELOAD_METADATA = True
AWS_ACCESS_KEY_ID = config('AWSAccessKeyId','')
AWS_SECRET_ACCESS_KEY = config('AWSSecretKey','')
AWS_STORAGE_BUCKET_NAME = 'everton-djangoecommerce'
AWS_S3_CUSTOM_DOMAIN = 's3.amazonaws.com/%s' %AWS_STORAGE_BUCKET_NAME

STATICFILES_STORAGE ='djangoecommerce.s3util.StaticStorage'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN,STATICFILES_LOCATION)

DEFAULT_FILE_STORAGE = 'djangoecommerce.s3util.MediaStorage'
MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN,MEDIAFILES_LOCATION)

AWS_S3_OBJECT_PARAMETERS={
    'x-amz-acl': 'public-read',
    'CacheControl':'public, max-age=31556926'
}




STATICFILES_DIRS = [
    os.path.join(BASE_DIR,"static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'everton_s.d@hotmail.com'


AUTH_USER_MODEL = 'accounts.User'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.ModelBackend',    
]

from django.contrib.messages import constants as messages_constants

MESSAGE_TAGS = {
    messages_constants.DEBUG:'debug',
    messages_constants.INFO:'info',
    messages_constants.SUCCESS:'success',
    messages_constants.WARNING:'warning',
    messages_constants.ERROR:'danger',
}

#pagseguro
PAGSEGURO_TOKEN = '4DA5ECE3B9544A818E8C7323E15C8D15'
PAGSEGURO_EMAIL = 'everton_s.d@hotmail.com'
PAGSEGURO_SANDBOX = True

#PayPal configuração
PAYPAL_TEST = True
PAYPAL_EMAIL = 'everton_s.d@hotmail.com'


THUMBNAIL_ALIASES = {
    '': {
        'product_image': {'size': (350, 200), 'crop': True},
    },
}

THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE

