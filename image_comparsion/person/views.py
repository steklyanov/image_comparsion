from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PersonSerializer
from .models import Person


class PersonRegistration(APIView):
    """ View to create a new user object"""

    @staticmethod
    def post(request):
        person_instance = PersonSerializer(data=request.data)
        if person_instance.is_valid():
            person = Person(name=request.data['name'], surname=request.data['surname'])
            person.save()
            return Response(person.id, status=status.HTTP_201_CREATED)
        return Response(person_instance.errors, status=status.HTTP_400_BAD_REQUEST)
