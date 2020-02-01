from django.urls import path, include
from .views import PersonRegistration, ListAllUsersView, ListUserById

urlpatterns = [
    path('create/', PersonRegistration.as_view()),
    path('list/', ListAllUsersView.as_view()),
    path('details/<id>', ListUserById.as_view())
]
