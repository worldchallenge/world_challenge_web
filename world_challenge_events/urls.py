from django.urls import include, path
from .views import (
    EventListView,
    EventCreateFormView,
    EventDetailView,
)
from . import models

urlpatterns = [
    path('list/', EventListView.as_view(), name='event-list'), 
    path('create/', EventCreateFormView.as_view(),
         name='create-event'),
    path('detail/<uuid:pk>/', EventDetailView.as_view(),
         name='event-detail'),
    path('<event_id>/up/', EventDetailView.as_view(), name='event-vote-up'),

]
