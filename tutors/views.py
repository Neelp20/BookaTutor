from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from .models import Tutor, Subject


# tutors_list.html
class TutorListView(ListView):
    """Display all tutors, with optional subject filter"""
    model = Tutor
    template_name = "tutors/tutors_list.html"
    context_object_name = "tutors"

    def get_queryset(self):
        user = self.request.user
        queryset = Tutor.objects.all()

        # Hide admin/staff tutors for non-admin users
        if not user.is_superuser:
            queryset = queryset.filter(user__is_superuser=False, user__is_staff=False)

        # Subject filter
        subject_filter = self.request.GET.get('subject')
        if subject_filter:
            queryset = queryset.filter(subjects__name__iexact=subject_filter)

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        """Add subjects to context for dropdown filter"""
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()
        context['selected_subject'] = self.request.GET.get('subject', '')
        return context


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
    success_url = reverse_lazy('tutors-list')

    def form_valid(self, form):
        tutor_exists = Tutor.objects.filter(user=self.request.user).exists()
        if tutor_exists:
            messages.error(self.request, "You already have a tutor profile.")
            return redirect('tutors-list')
        form.instance.user = self.request.user
        return super().form_valid(form)


# update_tutor.html
class TutorUpdateView(UpdateView):
    """Edit a tutor profile"""
    model = Tutor
    fields = ['bio', 'subjects', 'hourly_rate', 'availability']
    template_name = "tutors/update_tutor.html"
    success_url = reverse_lazy('tutors-list')

    def get_queryset(self):
        return Tutor.objects.filter(user=self.request.user)


# delete_tutor.html
class TutorDeleteView(DeleteView):
    """Delete a tutor profile"""
    model = Tutor
    template_name = "tutors/delete_tutor.html"
    success_url = reverse_lazy('tutors-list')

    def get_queryset(self):
        return Tutor.objects.filter(user=self.request.user)

