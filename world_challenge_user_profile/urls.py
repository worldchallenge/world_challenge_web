from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView
from .views import (
    SignupView,
    LogoutView,
    activate,
)

urlpatterns = [
        path('profiles/signup/', views.SignupView.as_view(), name='signup'),
        path('profiles/signup/confirm/',
                      TemplateView.as_view(template_name='confirm.html'),
                      name='confirm'),
        re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/'
                            '(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                            activate,
                            name='activate'),
        path('profiles/logout',
                      LogoutView.as_view(),
                      name='logout'),
#    path(
#       '',
#        WorldChallengeUserProfileView.as_view(),
#        name='world_challenge_user_profile'),
]
