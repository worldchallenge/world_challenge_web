from django.shortcuts import redirect, render
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic.edit import FormView, UpdateView, CreateView
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model
from django.contrib import messages 
from django.core import serializers

from .models import Profile
from .forms import ProfileUpdateForm, ProfileCreateForm

User = get_user_model()

class ProfileListView(ListView):
    """ Profile line up."""
    
    template_name = 'world_challenge_profile/profile_list.html'
    queryset = User.objects.all() 
    context_object_name = 'total_profile_list'
    paginate_by = 50


class ProfileDetailView(DetailView):
    """ A page displaying individual profiles.
    """

    model = Profile 
    template_name = 'world_challenge_profile/profile_detail.html'
    context_object_name = 'profile_set'
    success_url = '/detail/<pk>'
    data = Profile.objects.all()



class ProfileCreateView(FormView):

    form_class = ProfileCreateForm
    template_name = 'world_challenge_profile/profile_form.html'

    def form_valid(self, form):
        form.save(self, request.user)
        return super(ProfileCreateView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse("profile-detail")


class ProfileUpdateView(UpdateView):
    """ Enables Update
        Denied if user is not Owner.
    """
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'world_challenge_profile/profile_update.html'


    def get_object(self, *args, **kwargs):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return user.profile

    def get_success_url(self, *args, **kwargs):
        return reverse("profile-list")



