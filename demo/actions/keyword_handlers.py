from response.core.models.incident import Incident
from django.conf import settings

from response.slack.models import CommsChannel
from response.slack.decorators import keyword_handler