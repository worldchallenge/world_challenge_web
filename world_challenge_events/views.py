
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from vote.models import Vote

from .forms import CreateEventForm
from .models import Event



class EventListView(ListView):
    """Shows Events lined up."""

    context_object_name = 'total_event_list'
    queryset = Event.objects.order_by('date')
    paginate_by = 50
    template_name = 'world_challenge_events/event_list.html'


class EventCreateFormView(View):
    """This view handles app logic for event creation"""

    model = Event
    form_class = CreateEventForm
    template_name = "world_challenge_events/event_create.html"
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.owner = User.objects.get(username=request.user)
            event.save()
            messages.success(request, 'Your event was successfully created')
            return HttpResponseRedirect(
                '/event/list/')
        else:
            return HttpResponseRedirect(
                'world_challenge_events/event_create_error.html')
        return render(request, self.template_name, {'form': form})


class EventDetailView(DetailView):
    """Home page for individual events"""

    model = Event

    def post(self, request, *args, **kwargs):
        event = Event.objects.get(pk=kwargs['pk'])
        event.votes.up(request.user.id)
        messages.success(request, "Thank you for voting!")
        return HttpResponseRedirect('/event/list/')


class OwnershipMixin(object):
    """
    Mixin providing a dispatch overload that checks object ownership. is_staff and is_supervisor
    are considered object owners as well. This mixin must be loaded before any class based views
    are loaded for example class SomeView(OwnershipMixin, ListView)
    """
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        # we need to manually "wake up" self.request.user which is still a SimpleLazyObject at this point
        # and manually obtain this object's owner information.
        current_user = self.request.user._wrapped if hasattr(self.request.user, '_wrapped') else self.request.user
        object_owner = getattr(self.get_object(), 'owner')

        if current_user != object_owner and not current_user.is_superuser and not current_user.is_staff:
            raise PermissionDenied
        return super(OwnershipMixin, self).dispatch(request, *args, **kwargs)
