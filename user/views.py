from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy
from .models import UserProfile
from .forms import UserProfileForm


@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'users/profile_detail.html'

    def get_object(self):
        return self.request.user.userprofile


@method_decorator(login_required, name='dispatch')
class ProfileEditView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'users/profile_edit.html'
    success_url = reverse_lazy('profile-detail')

    def get_object(self):
        return self.request.user.userprofile
