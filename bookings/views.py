from django.shortcuts import render

# Create your views here.


def bookings(request):
    """ A view to return the bookings page """

    return render(request, 'bookings/bookings.html')
