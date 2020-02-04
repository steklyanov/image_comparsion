from django.urls import path, include
from .views import PersonRegistration, ListAllUsersView, ListUserById, \
    ImageUploadView, EuclideanDistanceView, DeleteUserById

app_name = 'person'

urlpatterns = [
    path('create/', PersonRegistration.as_view(), name='create'),
    path('list/', ListAllUsersView.as_view(), name='list'),
    path('details/<id>/', ListUserById.as_view(), name='details'),
    path('details/<id>/upload/', ImageUploadView.as_view(), name='upload'),
    path('distance/<id1>/<id2>/', EuclideanDistanceView.as_view(), name='distance'),
    path('details/<id>/delete/', DeleteUserById.as_view(), name='delete')
]
