from response.slack import block_kit
from response.slack.decorators import headline_post_action

#remove this before committing as its testing
@headline_post_action(order=150)
def my_cool_headline_action(headline_post):
    return block_kit.Button(":sparkles: My cool action inside custom file", "my-cool-action", value=headline_post.incident.pk)