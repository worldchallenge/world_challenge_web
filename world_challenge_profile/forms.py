from django import forms

from .models import  Profile 
from django.contrib.auth.models import User

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile 
        exclude = ('user','date', 'owner')
