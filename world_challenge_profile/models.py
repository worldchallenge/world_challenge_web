from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User, AbstractUser  


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=200, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    date = models.DateTimeField(default=datetime.now)
    avatar = models.ImageField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'pk': self.pk})
