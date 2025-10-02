from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tutor
from django.shortcuts import render

# Create your views here.


# def tutors_list(request):
#     """View to list all tutors"""
#     return render(request, 'tutors/tutors_list.html')

# tutors_list.html
class TutorListView(ListView):
    """Display all tutors"""
    model = Tutor
    template_name = "tutors/tutors_list.html"
    context_object_name = "tutors"


# tutor_detail.html
class TutorDetailView(DetailView):
    """Display details for one tutor"""
    model = Tutor
    template_name = "tutors/tutor_detail.html"
    context_object_name = "tutor"


# create_tutor.html
class TutorCreateView(CreateView):
    """Create a tutor profile"""
    model = Tutor
    fields = ['bio', 'subjects', 'hourly_rate', 'availability']  
    template_name = "tutors/create_tutor.html"
    success_url = reverse_lazy('tutor-list')

    def form_valid(self, form):
        # Auto-link tutor to logged in user
        form.instance.user = self.request.user
        return super().form_valid(form)


# update_tutor.html
class TutorUpdateView(UpdateView):
    """Edit a tutor profile"""
    model = Tutor
    fields = ['bio', 'subjects', 'hourly_rate', 'availability']
    template_name = "tutors/update_tutor.html"
    success_url = reverse_lazy('tutor-list')

    def get_queryset(self):
        # Only allow tutors to edit their own profile
        return Tutor.objects.filter(user=self.request.user)


# delete_tutor.html
class TutorDeleteView(DeleteView):
    """Delete a tutor profile"""
    model = Tutor
    template_name = "tutors/delete_tutor.html"
    success_url = reverse_lazy('tutor-list')

    def get_queryset(self):
        # Tutors can only delete their own profile
        return Tutor.objects.filter(user=self.request.user)
