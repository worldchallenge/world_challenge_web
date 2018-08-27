from django.shortcuts import render

from django.views import View

from django.views.generic import RedirectView

from django.contrib.auth import (
    logout as auth_logout
)


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
