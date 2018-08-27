from django.urls import include, path
from .views import EventListView


urlpatterns = [
    path('', EventListView.as_view(), name='event-list'),
]
