from django.urls import path, include
from .views import (
    ProfileListView, 
    ProfileDetailView,
    ProfileCreateUpdateView,
)

urlpatterns = [
    path('list/', ProfileListView.as_view(), name='profile-list' ),
    path('detail/<pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('update', ProfileCreateUpdateView.as_view(), name='profile-update'),
        
        ]
