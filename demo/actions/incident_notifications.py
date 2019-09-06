from response.core.models import Incident
from response.slack.models import CommsChannel
from response.slack.decorators import recurring_notification, single_notification

#remove this before committing as its testing
@recurring_notification(interval_mins=1, max_notifications=10)
def remind_severity(incident: Incident):
    try:
        comms_channel = CommsChannel.objects.get(incident=incident)
        if not incident.severity:
            comms_channel.post_in_channel(
                "Test one minute recurring notification from custom file...`")
    except CommsChannel.DoesNotExist:
        pass