import os

from django.core.wsgi import get_wsgi_application
from .actions.headline_actions import *
from .actions.incident_commands import *
from .actions.incident_notifications import *
from .actions.keyword_handlers import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'incidentresponse.settings.dev')

application = get_wsgi_application()
