from django.urls import path
from .views import TutorListView, TutorDetailView, TutorCreateView
from .views import TutorUpdateView, TutorDeleteView


urlpatterns = [
    # path('', views.tutors_list, name='tutors_list'),
    path('', TutorListView.as_view(), name='tutors-list'),
    path('<int:pk>/', TutorDetailView.as_view(), name='tutor-detail'),
    path('create/', TutorCreateView.as_view(), name='create-tutor'),
    path('edit/<int:pk>/', TutorUpdateView.as_view(), name='edit-tutor'),
    path('delete/<int:pk>/', TutorDeleteView.as_view(), name='delete-tutor'),
]
