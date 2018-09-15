from django.urls import include, path
from .views import (
    EventListView,
    EventCreateFormView,
    EventDetailView,
    EventUpdateView,
)
from . import models

urlpatterns = [
    path('list/', EventListView.as_view(), name='event-list'), 
    path('create/', EventCreateFormView.as_view(), name='event-create'),
    path('detail/<pk>/', EventDetailView.as_view(), name='event-detail'),
    path('detail/<pk>/update', EventUpdateView.as_view(), name='event-update'),

]
