from datetime import datetime

from django.db import models
from vote.models import VoteModel
from vote.managers import VotableManager
from django.conf import settings

class Event(VoteModel, models.Model):
    """Creates an event and saves the user event to /var/www"""

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=400, blank=True)
    date = models.DateTimeField(default=datetime.now)
    file_upload = models.FileField(upload_to='media', blank=True)
