from django.utils import timezone
from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Event


class EventListView(ListView):

    model = Event
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
