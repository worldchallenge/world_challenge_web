from django.urls import include, path
from .views import (
    EventListView,
    CreateEventFormView,
    EventDetailView,
)
from . import models

urlpatterns = [
    path('list/', EventListView.as_view(), name='event-list'), 
    path('create/', CreateEventFormView.as_view(),
         name='create-event'),
    path('detail/<uuid:pk>/',EventDetailView.as_view(),
         name='event-detail'),

]
