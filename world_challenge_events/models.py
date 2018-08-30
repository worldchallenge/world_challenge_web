from django.db import models



class Event(models.Model):
    """Creates an event and saves the user event to /var/www"""

    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=400, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    file_upload = models.FileField(upload_to='media', blank=True)
