from django.http import Http404

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser

from .serializers import PersonSerializer, ListIdSerializer, ImageSerializer
from .models import Person

from PIL import Image
import numpy as np
import cv2


class PersonRegistration(APIView):
    """ View to create a new user object"""

    @staticmethod
    def post(request):
        print(request.data['name'])
        person_instance = PersonSerializer(data=request.data)
        if person_instance.is_valid():
            person = Person(name=request.data['name'], surname=request.data['surname'])
            person.save()
            return Response(person.id, status=status.HTTP_201_CREATED)
        return Response(person_instance.errors, status=status.HTTP_400_BAD_REQUEST)


class ListAllUsersView(generics.ListAPIView):
    serializer_class = ListIdSerializer
    queryset = Person.objects.all()


class ListUserById(APIView):
    """ Show user by id in url path"""
    def get_object(self, id):
        try:
            return Person.objects.get(id=id)
        except:
            raise Http404

    def get(self, request, id, format=None):
        person = self.get_object(id)
        serializer = PersonSerializer(person)
        return Response(serializer.data)


class ImageUploadView(APIView):
    """ View for uploading image"""
    parser_class = (MultiPartParser,)

    def put(self, request, id):

        file_serializer = ImageSerializer(data=request.data)
        print(id)
        if file_serializer.is_valid():
            x = np.fromstring(request.data['image'].read(), dtype='uint8')
            img = cv2.imdecode(x, cv2.IMREAD_UNCHANGED).astype(np.float32) / 255
            flat_arr = img.ravel()
            person = Person.objects.get(id=id)
            vector = flat_arr.tolist()
            print(len(vector))
            print(type(vector))
            # person.vector =
            # person.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
