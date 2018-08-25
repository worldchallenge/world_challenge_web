from django.contrib.sites.shortcuts import get_current_site

from django.shortcuts import render, redirect

from django.utils.encoding import force_bytes

from django.utils.http import urlsafe_base64_encode

from django.template.loader import render_to_string

from django.http import HttpResponse

from django.template import loader

from django.views.generic.base import TemplateView

from django.views import View

from world_challenge_user_profile.models import User

from .forms import SignUpForm

from .tokens import account_activation_token

import sendgrid

import os

from sendgrid.helpers.mail import *


class HomeView(TemplateView):
    """Establishing simple HomeView that will surely be expanded later as
       site complexity increases.
    """

    template_name = 'home.html'


class SignupView(View):
    """This view implements Signup functionality.."""

    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

    def signup(self, request):
        """If POST and form is filled out then email is sent to user.  If not
           then user is presented with form to complete."""

        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                subject = "Welcome to the World Challenge Contest!"
                content = render_to_string('account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                mail = Mail(from_email, subject, to_email, content)
                sg.client.mail.send.post(request_body=mail.get())
                return redirect('account_activation_sent')
        else:
            form = SignUpForm()
        return render(request, 'signup.html', {'form':form}

def account_activation_sent(request):
    """Handles view for sent activation email to user."""

    return render(request, 'account_activation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = user.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)

        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')

