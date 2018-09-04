from django.urls import include, path
from .views import (
    EventListView,
    CreateEventFormView,
    EventDetailView,
)
from . import models

urlpatterns = [
    path('', EventListView.as_view(), name='event-list'),
    path('event_list/create_event/', CreateEventFormView.as_view(),
         name='create-event'),
    path('event_list/event_detail/<uuid:pk>/',EventDetailView.as_view(),
         name='event-detail'),

]
