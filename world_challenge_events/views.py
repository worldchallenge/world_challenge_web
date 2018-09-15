from django.views.generic.edit import UpdateView, CreateView
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from vote.models import Vote

from .forms import EventCreateForm
from .models import Event



class EventListView(ListView):
    """Shows Events lined up."""

    context_object_name = 'total_event_list'
    queryset = Event.objects.order_by('date')
    paginate_by = 50
    template_name = 'world_challenge_events/event_list.html'


class EventCreateFormView(CreateView):
    """This view handles app logic for event creation"""

    model = Event
    form_class = EventCreateForm
    template_name = "world_challenge_events/event_create.html"


class EventDetailView(DetailView):
    """Home page for individual events"""

    model = Event

    def post(self, request, *args, **kwargs):
        event = Event.objects.get(pk=kwargs['pk'])
        event.votes.up(request.user.id)
        return HttpResponseRedirect('/event/list/')


class EventUpdateView(UpdateView):
    """ Enables owner to edit their event. Raise Permission
        Denied if user is not Owner.
    """
    
    model = Event
    form_class = EventCreateForm
    template_name = 'world_challenge_events/event_update.html'

    def dispatch(self, request, *args, **kwargs):
        event = Event.objects.get(pk=kwargs['pk'])
        if event.owner != self.request.user:
            raise Http404('Permission Denied!!')
        return super(EventUpdateView, self).dispatch(request, *args, **kwargs)


