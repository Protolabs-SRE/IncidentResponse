from response.core.models import Incident
from response.slack.decorators.incident_command import incident_command

#remove this before committing as its testing
@incident_command(['here'], helptext='Are you there?')
def are_you_here(incident: Incident, user_id: str, message: str):
    return True, "I'm here and in a custom file"