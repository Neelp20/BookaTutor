from django.shortcuts import render

# Create your views here.


def tutors_list(request):
    """View to list all tutors"""
    return render(request, 'tutors/tutors_list.html')
