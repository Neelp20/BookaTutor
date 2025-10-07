from django.urls import path
from .views import ProfileDetailView, ProfileUpdateView

urlpatterns = [
    path('profile/', ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile-edit'),
]
