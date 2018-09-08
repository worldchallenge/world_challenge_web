from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required

from .forms import CreateEventForm
from .models import Event
from vote.models import Vote


VOTE = (('up', 1), ('down', -1), ('clear', 0))


class EventListView(ListView):
    """Shows Events lined up."""

    context_object_name = 'total_event_list'
    queryset = Event.objects.order_by('name')
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
            return HttpResponseRedirect(
                '/event/list/')
        else:
            return HttpResponseRedirect(
                'world_challenge_events/event_create_error.html')
        return render(request, self.template_name, {'form': form})


class EventDetailView(DetailView):
    """Home page for individual events"""

    model = Event

    def get_event_detail(self, request, primary_key):
        event = get_object_or_404(Event, pk=primary_key)
        return render(request, 'world_challenge_events/event_detail.html',
                      context={'event': event})


class VoteView(View):
    """Class manages voting"""

    @login_required
    def vote_on_object(request, app, object_id, vote):
        """
        Generic object vote function
        """
        
        next = request.REQUEST.get('next', None)
        if not next:
            next = request.META.get('HTTP_REFERER', None)
        if not next:
            next = '/'
        
        print app
        
        try:
            app_label, model = app.split('_')
            ctype = ContentType.objects.get(app_label=app_label, model=model)
        except ContentType.DoesNotExist:
            return HttpResponseRedirect(next + '?error=app-not-exists')
            
        klass = ctype.model_class()
        
        try:
            Vote.objects.record_vote(klass.objects.get(pk=object_id), request.user, dict(VOTE)[vote])
        except klass.DoesNotExist:
            return HttpResponseRedirect(next + '?error=object-not-exists')
        except KeyError:
            return HttpResponseRedirect(next + '?error=vote-not-valid')
        except ValueError:
            return HttpResponseRedirect(next + '?error=vote-not-valid')
        
        return HttpResponseRedirect(next + '?success=vote-registered')
