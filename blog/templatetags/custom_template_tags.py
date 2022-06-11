import re
from django import template

register = template.Library()


@register.filter(name="embedurl")
def get_embed_url_with_parameters(url):
    if "youtube.com" in url or "youtu.be" in url:
        # Get video id from URL
        regex = r"(?:https:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?(.+)"
        embed_url = re.sub(
            regex, r"https://www.youtube.com/embed/\1", url
        )  # Append video id to desired URL
        embed_url_with_parameters = embed_url + "?rel=0"  # Add additional parameters
        return embed_url_with_parameters
    else:
        return None
