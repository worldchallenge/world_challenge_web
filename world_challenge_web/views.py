from django.shortcuts import render, redirect

from django.core.mail import EmailMessage
from django.urls import reverse

from django.http import HttpResponse, HttpResponseRedirect

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.template.loader import render_to_string

from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout as auth_logout
)

from django.contrib.sites.shortcuts import get_current_site

from django.views.generic import RedirectView
from django.views import View

from world_challenge_user_profile.tokens import account_activation_token
from world_challenge_user_profile.models import User
from world_challenge_user_profile.forms import SignupForm


class HomeView(View):
    template_name = 'home.html'
    context = {}

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
        return render(request, self.template_name, self.context)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)




