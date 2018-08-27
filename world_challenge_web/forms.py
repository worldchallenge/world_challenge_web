from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class SignupForm(UserCreationForm):
    """Simple signup form implementing activated email"""

    email = forms.EmailField(label="Email", max_length=200,
                             help_text='Required')
    state_province = forms.CharField(label='State/Province',
                                     max_length=200)
    country = forms.CharField(label="Country", max_length=200,
                              help_text='Required')
    phone = forms.IntegerField(label="Phone number")
    avatar = forms.ImageField(label="Avatar")

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
