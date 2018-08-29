from django.urls import include, path
from .views import EventListView


urlpatterns = [
    path('', EventListView.as_view(), name='event-list'),
    path('/events/create_event/', CreateEventView.as_view(),
         name='create-event')
]
