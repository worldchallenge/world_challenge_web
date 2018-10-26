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
from .forms import ProfileUpdateForm

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



class ProfileUpdateView(CreateView):
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
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ProfileUpdateForm(request.POST,
                    instance=Profile.objects.get(user=request.user))
            if form.is_valid():
                form.clean()
                #form.owner = True
                form.save()
                messages.add_message(request, messages.INFO, 'Success!')
                return render(request, 'world_challenge_profile/profile_list.html', {'form':form})
            else:
                form = ProfileUpdateForm(instance=request.user.profile)
                return render(request, 'world_challenge_profile/profile_update.html', {'form':form})
        return render(request, 'world_challenge_profile/profile_update.html', {'form':form})





