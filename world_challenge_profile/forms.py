from django import forms

from .models import  Profile 

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile 
        exclude = ('user','date')

    def save(self, user=None):
        user_profile = super(ProfileUpdateForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()


class ProfileCreateForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ('user','date')
