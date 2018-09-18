from django import template

from django.contrib.auth.models import AnonymousUser
from django import get_version
from vote.models import Vote

register = template.Library()


