from .base import *

SECRET_KEY = "j&8vqzrt_9-bngny95u2mu*gsfdu8%f*h5tl=c*qit_oa9h0r+"

DEBUG_MODE=True

ALLOWED_HOSTS=['localhost','127.0.0.1','0.0.0.0']
CSRF_TRUSTED_ORIGINS = ['http://localhost:8069']

CORS_ALLOWED_ORIGINS = CSRF_TRUSTED_ORIGINS

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'neondb',
    'USER': 'freitasanderson',
    'PASSWORD': '5h7yquaQdCrg',
    'HOST': 'ep-late-bread-25683911.us-east-2.aws.neon.tech',
    'PORT': '5432',
  }
}