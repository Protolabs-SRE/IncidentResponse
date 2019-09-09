from response.core.models.incident import Incident
from django.conf import settings

from response.slack.models import CommsChannel
from response.slack.decorators import keyword_handler

import logging
logger = logging.getLogger(__name__)


@keyword_handler(['status page', 'statuspage'])
def status_page_notification(comms_channel: CommsChannel, user: str, text: str, ts: str):
    comms_channel.post_in_channel(f"ℹ️ You mentioned the Status Page - <{settings.STATUS_PAGE_RUNBOOK_URL}|here's the playbook> on how to put it up.")

@keyword_handler(['run book', 'runbook', 'play book', 'playbook'])
def status_page_notification(comms_channel: CommsChannel, user: str, text: str, ts: str):
    comms_channel.post_in_channel(f"ℹ️ You mentioned playbook(s) - <{settings.RUNBOOKS_URL}|here's the playbook(s)> location.")