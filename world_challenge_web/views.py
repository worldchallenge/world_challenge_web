from django.shortcuts import render
from django.views.generic.base import TemplateView

from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout as auth_logout
)


class HomeView(TemplateView):
    template_name = "world_challenge_web/home.html"
    context = {}

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
        return render(request, self.template_name, self.context)
