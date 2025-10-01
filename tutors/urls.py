from django.urls import path 
from . import views

urlpatterns = [
    path('', views.tutors_list, name='tutors_list'),
]