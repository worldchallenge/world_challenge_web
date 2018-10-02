from django_registration.forms import RegistrationForm 
from django.contrib.auth import get_user_model


class RegisterForm(RegistrationForm):
    """Simple signup form implementing activated email"""


    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')
