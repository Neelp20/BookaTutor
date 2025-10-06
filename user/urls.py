from django.contrib import admin
from .views import (
    UserCreateView,
)


urlpatterns = [
    path('', UserCreateView.as_view(), name='user'),
]
