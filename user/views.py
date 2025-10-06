# users/views.py
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy
from .models import Profile
from .forms import ProfileForm


@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'users/profile_detail.html'

    def get_object(self):
        return self.request.user.profile


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'users/profile_edit.html'
    success_url = reverse_lazy('profile-detail')

    def get_object(self):
        return self.request.user.profile
