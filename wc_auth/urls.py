from django.urls import path, include
from .views import (
        LogoutView, 
        RegisterView,
        ActivateView,
        )
from django.views.generic.base import TemplateView

urlpatterns = [
    path('logout/', LogoutView.as_view()),
    path('accounts/', include(
        'django_registration.backends.activation.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/register/disallowed/',
        TemplateView.as_view(template_name='registration_error.html')),
    path('accounts/register/activateion_complete/',
        TemplateView.as_view(template_name='registration_complete.html')),
    path('accounts/activate/<activation_key>', ActivateView.as_view(),
        name='activate'), 
    path('accounts/activate/activation_complete/',
        TemplateView.as_view(template_name='activation_complete.html')),
    ]
