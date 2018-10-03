from django.urls import path, include


urlpatterns = [
    path('list/', ProfileListView.as_view(), name='profile' ),
        
        ]
