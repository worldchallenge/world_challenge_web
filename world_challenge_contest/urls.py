from django.contrib import admin
from django.urls import include, path
from django.conf import settings

if settings.DEBUG:
    import debug_toolbar
urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('', include('world_challenge_web.urls')),
    path('event/', include('world_challenge_events.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('wc_auth.urls')),
    path('profile/', include('world_challenge_profile.urls')),
]
