from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import UserProfile
from .forms import UserProfileForm


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'users/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return self.request.user.userprofile


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'users/profile_edit.html'
    success_url = reverse_lazy('profile-detail')

    def get_object(self, queryset=None):
        return self.request.user.userprofile
