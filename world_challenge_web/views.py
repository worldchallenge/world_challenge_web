from django.http import HttpResponse

from django.template import loader

from django.views.generic.base import TemplateView

from world_challenge_user_profile.models import User


class HomeView(TemplateView):
    """Establishing simple HomeView that will surely be expanded later as
    site complexity increases."""

    template_name = 'home.html'




