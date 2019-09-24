from .base import *

DEBUG = False

if os.environ.get("POSTGRES"):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': os.environ.get("DB_HOST"),
            'PORT': os.environ.get("DB_PORT"),
            'USER': os.environ.get("DB_USER"),
            'NAME': os.environ.get("DB_NAME"),
            'PASSWORD': os.environ.get("DB_PASSWORD"),
            'SSLMODE': os.environ.get("DB_SSL_MODE")
        }
    }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': " {levelname:5s} - {module:10.15s} - {message}",
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}
