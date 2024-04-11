from __future__ import absolute_import, unicode_literals
import os

from .base import *
import dj_database_url

DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'

# Allow all host headers
ALLOWED_HOSTS = ['*']

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

DEBUG = False

# Amazon S3 Credentials
AWS_ACCESS_KEY_ID = env['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = env['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = env['AWS_STORAGE_BUCKET_NAME']
AWS_S3_SIGNATURE_NAME = 's3v4',
AWS_S3_REGION_NAME = env['AWS_S3_REGION_NAME']
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL =  None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Wagtail Recaptcha Credentials
RECAPTCHA_PUBLIC_KEY = env['RECAPTCHA_PUBLIC_KEY']
RECAPTCHA_PRIVATE_KEY = env['RECAPTCHA_PRIVATE_KEY']
NOCAPTCHA = True

try:
    from .local import *
except ImportError:
    pass


print("DEBUG =",DEBUG)