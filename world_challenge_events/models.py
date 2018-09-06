from django.db import models
import uuid

from django.contrib.auth.models import User
from datetime import datetime



class Event(models.Model):
    """Creates an event and saves the user event to /var/www"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=400, blank=True)
    date = models.DateTimeField(default=datetime.now)
    file_upload = models.FileField(upload_to='media', blank=True)
