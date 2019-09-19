import os

from django.core.wsgi import get_wsgi_application
from .actions.headline_actions import *
from .actions.incident_commands import *
from .actions.incident_notifications import *
from .actions.keyword_handlers import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'incidentresponse.settings.dev')

application = get_wsgi_application()

# dirty hackery is afoot here. This is modifying monzo's channel create functionality to be our own
from response.slack.models.comms_channel import CommsChannelManager
from urllib.parse import urljoin
from django.urls import reverse
from django.conf import settings
import time
from response.slack.client import SlackError
import logging


def create_incident_our_way(self, incident):
    """Creates a comms channel in slack, and saves a reference to it in the DB"""
    logger = logging.getLevelName("protolabs.custom.slackchannelcreator")
    try:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        name = f"inc-{timestamp}"
        channel_id = settings.SLACK_CLIENT.get_or_create_channel(name, auto_unarchive=True)
    except SlackError as e:
        logger.error('Failed to create comms channel {e}')

    try:
        doc_url = urljoin(
            settings.SITE_URL,
            reverse('incident_doc', kwargs={'incident_id': incident.pk})
        )

        settings.SLACK_CLIENT.set_channel_topic(channel_id, f"{incident.report} - {doc_url}")
    except SlackError as e:
        logger.error('Failed to set channel topic {e}')

    comms_channel = self.create(
        incident=incident,
        channel_id=channel_id,
    )
    return comms_channel


CommsChannelManager.create_comms_channel = create_incident_our_way
