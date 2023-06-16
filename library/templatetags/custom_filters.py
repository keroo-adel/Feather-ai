from django import template
from django.utils.timesince import timesince
from datetime import datetime, timezone

register = template.Library()

@register.filter
def split_string(value, delimiter):
    return value.split(delimiter)

@register.filter
def has_any(value, items):
    return any(item in value for item in items)

@register.filter
def split_tags(tags):
    return tags.split(',')


@register.filter
def time_since_minutes(value):
    now = datetime.now(timezone.utc)
    if value < now:
        time_diff = timesince(value, now).split(",")[0]
        return f"Created {time_diff} ago"
    return "Just now"
