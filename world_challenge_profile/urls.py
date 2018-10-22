from django.urls import path, include
from .views import (
    ProfileListView, 
    ProfileDetailView,
    ProfileCreateUpdateView,
)

urlpatterns = [
    path('list/', ProfileListView.as_view(), name='profile-list' ),
    path('detail/<pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('update/<pk>/', ProfileCreateUpdateView.as_view(pk='pk'), name='profile-update'),
        
        ]
