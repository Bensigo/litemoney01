from .settings import *
import dj_database_urls
#adding production settings
DATABASES['default'] = dj_database_url.config()
DEBUG = False
TEMPLATE_DEBUG = True
#for static files and media files
STATICFILES_DIRS =(os.path.join(BASE_DIR,'static'),)
STATIC_ROOT = os.path.join(BASE_DIR,'static-cdn')
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
MEDIA_ROOT = os.path.join(BASE_DIR,'media-cdn')
MEDIA_URL = '/media/'

#putting the reqired domain hosting this site
ALLOWED_HOSTS =['www.LiteMoney.io','*']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO','https')



