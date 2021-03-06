from django import forms

from .models import Event

class EventCreateForm(forms.ModelForm):


    class Meta:
        model = Event
        fields = ('name', 'location', 'description', 'file_upload')
