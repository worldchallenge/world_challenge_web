from django.urls import path, include
from .views import (
    ProfileListView, 
    ProfileDetailView,
    ProfileUpdateView,
)

urlpatterns = [
    path('list/', ProfileListView.as_view(), name='profile-list' ),
    path('detail/<pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('update/<pk>/', ProfileUpdateView.as_view(), name='profile-update'),

        ]
