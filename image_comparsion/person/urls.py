from django.urls import path, include
from .views import PersonRegistration

urlpatterns = [
    path('create/', PersonRegistration.as_view()),
]
