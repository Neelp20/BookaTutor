from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterForm

# Create your views here.


def home(request):
    raise Exception("🔥 Manual test exception for 500 page")


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


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


def custom_500_view(request):
    return render(request, '500.html', status=500)
