from django import template
from django.conf import settings

import bleach


register = template.Library()


@register.filter
def clean(value):
    return bleach.clean(value, tags=settings.ALLOWED_TAGS)
