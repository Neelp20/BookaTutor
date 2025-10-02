from django.urls import path
from . import TutorListView, TutorDetailView, TutorCreateView
from . import TutorUpdateView, TutorDeleteView


urlpatterns = [
    # path('', views.tutors_list, name='tutors_list'),
    path('', TutorListView.as_view(), name='tutors-list'),
    path('<int:pk>/', TutorDetailView.as_view(), name='tutor-detail'),
    path('create/', TutorCreateView.as_view(), name='create-tutor'),
    path('edit/<int:pk>/', TutorUpdateView.as_view(), name='update-tutor'),
    path('delete/<int:pk>/', TutorDeleteView.as_view(), name='delete-tutor'),
]
