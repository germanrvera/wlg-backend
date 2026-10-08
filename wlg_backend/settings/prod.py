from .base import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='wlgled.com.ar').split(',')

# Database - Support both DATABASE_URL (Render/Railway) and individual config
if config('DATABASE_URL', default=None):
    DATABASES = {
        'default': dj_database_url.config(
            default=config('DATABASE_URL'),
            conn_max_age=600
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': config('DB_PORT', default='5432'),
        }
    }

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

# Cloudflare R2 — media storage
if config('R2_ACCESS_KEY_ID', default=None):
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_ACCESS_KEY_ID = config('R2_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('R2_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('R2_BUCKET_NAME')
    AWS_S3_ENDPOINT_URL = 'https://' + config('R2_ACCOUNT_ID') + '.r2.cloudflarestorage.com'
    AWS_S3_REGION_NAME = 'auto'
    AWS_DEFAULT_ACL = None
    AWS_S3_FILE_OVERWRITE = False
    AWS_QUERYSTRING_AUTH = False
    MEDIA_URL = config('R2_PUBLIC_URL') + '/'

SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=True, cast=bool)
SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=True, cast=bool)
CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', default=True, cast=bool)
