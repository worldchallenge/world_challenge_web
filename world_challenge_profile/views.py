from django.shortcuts import redirect, render
from django.http import Http404
from django.urls import reverse
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model
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

    model = User 
    template_name = 'world_challenge_profile/profile_detail.html'


class ProfileCreateUpdateView(UpdateView):
    """ Enables Update
        Denied if user is not Owner.
    """
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'world_challenge_profile/profile_form.html'
    success_url = '/profile/detail/<pk>/'
    pk = 'pk' 
    def get_queryset(self):
        return Profile.objects.all()

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ProfileUpdateForm(request.POST, instance=request.user)
            if form.is_valid():
                cleaned_data = Super(form, self).clean()
                obj = form.save(commit=False)
                obj.save()
                return render(request, get_success_url) 
            else:
                form = ProfileUpdateForm()
                return render(request, template_name, {'form': form})
        else:
            return redirect(request, 'profile/list') 
