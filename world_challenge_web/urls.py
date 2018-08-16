"""world_challenge_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView

from world_challenge_user_profile import urls as profile_urls

from world_challenge_user_profile.views import (
    HomeView,
    SignupView,
    LogoutView,
    activate,
)
urlpatterns = [
    path('profile/', include(profile_urls)),
    path('admin/', admin.site.urls),
    path(r'^$',
         HomeView.as_view(),
         name='home'),
    path(r'^logout/',
         LogoutView.as_view(),
         name='logout'),
    re_path(r'^activate/?P<uidb64>[0-9A-Za-z_\-]+)/'
            '(?P<token>[0-9A-Za-z]{1,13})-[0-9A-Za-z]{1,20})/$',
            activate,
            name='activate'),
    path(r'^signup/confirm/',
         TemplateView.as_view(template_name='confirm.html'),
         name='confirm'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

