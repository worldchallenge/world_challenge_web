from django.urls import include, path
from .views import (
    EventListView,
    EventCreateFormView,
    EventDetailView,
)
from . import models

urlpatterns = [
    path('list/', EventListView.as_view(), name='event-list'), 
    path('create/', EventCreateFormView.as_view(), name='event-create'),
    path('detail/<pk>/', EventDetailView.as_view(), name='event-detail'),

]
