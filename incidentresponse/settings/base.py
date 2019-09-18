import os
import logging
from response.slack.client import SlackClient
from django.core.exceptions import ImproperlyConfigured

# load from the environment 
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'after_response',
    'rest_framework',
    'bootstrap4',
    'response.apps.ResponseConfig',
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

ROOT_URLCONF = 'incidentresponse.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'incidentresponse.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

# Django Rest Framework
# https://www.django-rest-framework.org/

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ]
}

# Markdown Filter

MARKDOWN_FILTER_WHITELIST_TAGS = [
    'a',
    'p',
    'code',
    'h1',
    'h2',
    'ul',
    'li',
    'strong',
    'em',
    'img',
]

MARKDOWN_FILTER_WHITELIST_ATTRIBUTES = [
    'src',
    'style',
]

MARKDOWN_FILTER_WHITELIST_STYLES = [
    'width', 'height', 'border-color', 'background-color',
    'white-space', 'vertical-align', 'text-align',
    'border-style', 'border-width', 'float', 'margin',
    'margin-bottom', 'margin-left', 'margin-right', 'margin-top'
]


def get_env_var(setting, warn_only=False, default=None):
    value = os.getenv(setting, default)

    if not value and default is None:
        error_msg = f"ImproperlyConfigured: Set {setting} environment variable"
        if warn_only:
            logger.warn(error_msg)
        else:
            raise ImproperlyConfigured(error_msg)
    else:
        value = value.replace('"', '')  # remove start/end quotes

    return value


SITE_URL = get_env_var("SITE_URL", default="http://localhost:8000")
SLACK_TOKEN = get_env_var("SLACK_TOKEN")
SLACK_CLIENT = SlackClient(SLACK_TOKEN)
SLACK_SIGNING_SECRET = get_env_var("SLACK_SIGNING_SECRET")
INCIDENT_CHANNEL_NAME = get_env_var("INCIDENT_CHANNEL_NAME")
INCIDENT_BOT_NAME = get_env_var("INCIDENT_BOT_NAME")
SECRET_KEY = get_env_var("SECRET_KEY")
INCIDENT_BOT_ID = get_env_var("INCIDENT_BOT_ID", default=SLACK_CLIENT.get_user_id(INCIDENT_BOT_NAME))
INCIDENT_CHANNEL_ID = get_env_var("INCIDENT_CHANNEL_ID", default=SLACK_CLIENT.get_channel_id(INCIDENT_CHANNEL_NAME))
STATUS_PAGE_PLAYBOOK_URL = get_env_var("STATUS_PAGE_PLAYBOOK_URL")
PLAYBOOKS_URL = get_env_var("PLAYBOOKS_URL")
