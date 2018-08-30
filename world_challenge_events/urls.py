from django.urls import include, path
from .views import (
    EventListView,
    CreateEventFormView,
    EventDetailView,
)



urlpatterns = [
    path('', EventListView.as_view(), name='event-list'),
    path('create_event/', CreateEventFormView.as_view(), name='create-event'),
    path('event_home/<uuid:pk>',EventDetailView.as_view(), name='event-home'),

]
