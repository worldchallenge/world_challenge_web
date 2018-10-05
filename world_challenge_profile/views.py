from django.shortcuts import render
from django.http import Http404
from django.urls import reverse
from django.views.generic.edit import FormView
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

    model = Profile 
    template_name = 'world_challenge_profile/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        user = self.kwargs.get(self.pk_url_kwarg)
        queryset = Profile.objects.filter(user_id=user).values()
        context.update({'queryset': queryset})
        return context 

class ProfileCreateUpdateView(FormView):
    """ Enables Update
        Denied if user is not Owner.
    """

    form_class = ProfileUpdateForm
    template_name = 'world_challenge_profile/profile_form.html'
    success_url = '/profile/detail/<pk>'

    def post(self, request):
        if request.method == 'POST':
            form = get_form(ProfileUpdateFor(request.POST))
            if form_valid(form):
                context = get_context_data()
                return render_to_response(self, context)


    def get_form(self, form_class=ProfileUpdateForm):

        try:
            profile = Profile.objects.get(user=self.request.user)
            return form_class(**self.get_form_kwargs())
        except (Profile.IntegrityError, Profile.DoesNotExist) as e:
            return form_class(**self.get_form_kwargs())

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save(Profile.objects.all().update())
        return super(ProfileCreateUpdateView, self).form_valid(form)
