from django.utils import timezone
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponseRedirect

from .forms import CreateEventForm
from .models import Event


class EventListView(ListView):

    model = Event
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CreateEventFormView(View):
    """This view handles app logic for event creation"""

    form_class = CreateEventForm
    template_name = "create_event.html"
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})
