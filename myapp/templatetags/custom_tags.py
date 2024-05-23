from django import template
from urllib.parse import quote

register = template.Library()

@register.simple_tag
def facebook_share_url(content_url):
    base_url = "https://www.facebook.com/sharer/sharer.php"
    encoded_url = quote(content_url)
    return f"{base_url}?u={encoded_url}"
@register.simple_tag
def linkedin_share_url(content_url):
    base_url = "https://www.linkedin.com/sharer/sharer.php"
    encoded_url = quote(content_url)
    return f"{base_url}?u={encoded_url}"
@register.simple_tag
def twitter_share_url(content_url):
    base_url = "https://twitter.com/sharer/sharer.php"
    encoded_url = quote(content_url)
    return f"{base_url}?u={encoded_url}"