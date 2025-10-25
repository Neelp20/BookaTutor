from django.urls import path
from .views import ProfileDetailView, ProfileUpdateView

urlpatterns = [
    path('profile/', ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
]
