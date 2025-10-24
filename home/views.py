from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterForm

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def subscribe_newsletter(request):
    """ Handle newsletter form submission from footer """
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for subscribing!')
        else:
            messages.error(request, 'This email is already subscribed or invalid.')
    return redirect(request.META.get('HTTP_REFERER', 'home'))
