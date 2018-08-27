from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from . import views

from .forms import SignupForm

urlpatterns = [
    re_path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         views.activate,
         name='activate'),
    path('home/',
         views.HomeView.as_view(template_name='home.html'),
         name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'),
         name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'),
         name='logout'),
    path('accounts/profile/',
         TemplateView.as_view(template_name='profile.html'),
         name='profile'),
    path('accounts/password_reset/',
         TemplateView.as_view(template_name='registration/password_reset_form.html'),
         name='password_reset'),
    path('accounts/signup/', views.signup,
         name='signup'),
    path('accounts/account_activation_sent/',
         views.account_activation_sent,
         name='account_activation_sent'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
