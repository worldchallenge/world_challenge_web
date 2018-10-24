from django.urls import path, include
from .views import (
    ProfileListView, 
    ProfileDetailView,
    ProfileUpdateView,
    ProfileCreateView,
)

urlpatterns = [
    path('list/', ProfileListView.as_view(), name='profile-list' ),
    path('detail/<pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('update/<pk>/', ProfileUpdateView.as_view(), name='profile-update'),
    path('create/<pk>/', ProfileCreateView.as_view(), name='profile-create'),
        
        ]
