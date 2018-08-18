from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView

# from world_challenge_user_profile import urls as profile_urls

urlpatterns = [
    path('home/',
         TemplateView.as_view(template_name='home.html'),
         name='home'),
#    path('profile/', include(profile_urls)),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/',
         TemplateView.as_view(template_name='profile.html'),
         name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
