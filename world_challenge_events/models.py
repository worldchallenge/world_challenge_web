from django.db import models


def user_dir_path(instance, filename):
    """Uploads user file to their directory"""
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Event(models.Model):
    """Creates an event and saves the user event to their profile dir"""

    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=400)
    file_upload = models.FileField(upload_to=user_dir_path)
