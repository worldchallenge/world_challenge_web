from django.urls import path

from .views import WorldChallengeUserProfileView


urlpatterns = [
    path(
        '',
        WorldChallengeUserProfileView.as_view(),
        name='world_challenge_user_profile'),
]
