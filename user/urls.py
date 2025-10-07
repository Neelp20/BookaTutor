from django.urls import path
from .views import ProfileDetailView, ProfileEditView

urlpatterns = [
    path('', ProfileDetailView.as_view(), name='profile-detail'),
    path('edit/', ProfileEditView.as_view(), name='profile-edit'),
]
