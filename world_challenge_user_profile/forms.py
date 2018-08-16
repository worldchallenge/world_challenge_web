from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User


class SignupForm(UserCreationForm):
    first_name = forms.CharField(label='Enter first name', max_length=30, required=False)
    last_name = forms.CharField(label='Enter last name', max_length=30, required=False)
    email = forms.EmailField(label='Enter email', max_length=254, required=True )
    bio = forms.CharField(label='Enter bio', max_length=400, required=False)
    location = forms.CharField(label='Enter location', max_length=50, required=True)
    birth_date = forms.DateField(label='Enter birth date', required=False)
    avatar = forms.ImageField(label='Select avatar')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
				  'password2', 'bio', 'location', 'birth_date', 'avatar')
