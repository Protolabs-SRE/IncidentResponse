from response.core.models import Incident
from response.slack.models import CommsChannel
from response.slack.decorators import recurring_notification, single_notification

@recurring_notification(interval_mins=720, max_notifications=6)
def remind_close_incident(incident: Incident):
    try:
        comms_channel = CommsChannel.objects.get(incident=incident)
        if not incident.is_closed():
            comms_channel.post_in_channel(":timer_clock: This incident has been running a long time.  Can it be closed now?  Remember to pin important messages in order to create the timeline.")
    except CommsChannel.DoesNotExist:
        pass