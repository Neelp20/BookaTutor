from django.contrib import messages
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import UserProfile
from django.contrib.auth.models import User
from .forms import UserProfileForm


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'user/profile_edit.html'
    success_url = reverse_lazy('profile_detail')

    def get_object(self):
        return self.request.user.userprofile

    def form_valid(self, form):
        messages.success(self.request, "✅ Profile updated successfully!")
        return super().form_valid(form)
