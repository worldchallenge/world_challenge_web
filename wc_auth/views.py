from django.shortcuts import render

from django.views import View

from django.views.generic import RedirectView

from django_registration.exceptions import ActivationError, RegistrationError

from django.contrib.auth import (
    logout as auth_logout
)
from django_registration.backends.activation.views import (
        RegistrationView,
        ActivationView,
        )
from .forms import RegisterForm

class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class RegisterView(RegistrationView):
    """ Provides functionality to  Register/Signup.
    """
    form = RegisterForm()
    success_url = '/auth/accounts/registration/complete/'
    template_name = 'registration_complete.html'
    
    def register(self, request):
        if request.method == 'POST':
            if form.is_valid():
                registration_allowed(True)
                create_inactive_user(form)
                user = request.user.username
                user.user_registered()
                return render(get_success_url)
            else:
                registration_allowed(False)
                return RegistrationError(404, "Not allowed")
        else:
            messages.error(self, "Error in Form, Plese try again!")
            form = RegisterForm()
        return render(request, '/register/', {'form': form})


class ActivateView(ActivationView):
    """ Activates user if the link is selected from email.
    """
    
    success_url = '/auth/accounts/activate/activation_complete.html'
    template_name = 'django_registration/activation_complete.html'


