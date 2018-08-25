import sendgrid

import os

from django.contrib.sites.shortcuts import get_current_site

from django.shortcuts import render, redirect

from django.utils.encoding import force_bytes, force_text

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.template.loader import render_to_string

from django.http import HttpResponse

from django.template import loader

from django.views.generic.base import TemplateView

from django.views import View

from django.contrib.auth import get_user_model

from sendgrid.helpers.mail import *

from .forms import SignupForm

from .tokens import account_activation_token


class HomeView(TemplateView):
    """Establishing simple HomeView that will surely be expanded later as
       site complexity increases.
    """

    template_name = 'home.html'


def signup(request):
    """If POST and form is filled out then email is sent to user.  If not
       then user is presented with form to complete."""
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            to_email = Email("heckles83@gmail.com")
            from_email = Email("hecklerchris@hotmail.com")
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
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def account_activation_sent(self, request):
    """Handles view for sent activation email to user."""

    return render(request, 'account_activation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = user.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user,
                                                                 token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)

        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')
