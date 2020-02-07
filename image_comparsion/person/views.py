from django.http import Http404

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FileUploadParser, FormParser

from .serializers import PersonSerializer, ListIdSerializer, ImageSerializer
from .models import Person

import numpy as np
import cv2
from .tasks import save_vector_to_database, euclidean_distance


# NOT SURE ITS A GOOD PRACTISE, BUT I USE THIS FUNCTION IN MULTIPLE VIEWS
def get_object(uid):
    try:
        return Person.objects.get(id=uid)
    except:
        raise Http404


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

    def get(self, request, id, format=None):
        print(id)
        person = get_object(id)
        serializer = PersonSerializer(person)
        return Response(serializer.data)


class DeleteUserById(APIView):
    """ View for deleting person"""

    def delete(self, request, id):
        person = get_object(id)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ImageUploadView(APIView):
    """ View for uploading image"""
    parser_classes = (MultiPartParser, FileUploadParser, FormParser)

    def post(self, request, id, *args, **kwargs):
        file_serializer = ImageSerializer(data=request.data)
        if file_serializer.is_valid():
            x = np.fromstring(request.data['image'].read(), dtype='uint8')
            img = cv2.imdecode(x, cv2.IMREAD_UNCHANGED).astype(np.float32) / 255
            flat_arr = img.ravel()
            vector = flat_arr.tolist()
            save_vector_to_database.delay(id, vector)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EuclideanDistanceView(APIView):
    """ View to calculate Euclidean distance between arrays"""

    def get(self, request, id1, id2):
        print(id1)
        print(id2)
        person_1 = get_object(id1)
        person_2 = get_object(id2)
        if person_1.vector and person_2.vector:
            a = np.array(person_1.vector)
            b = np.array(person_2.vector)
            dist = np.linalg.norm(a-b)
            return Response(dist, status=status.HTTP_201_CREATED)
        return Response({'qq': 'qqq'}, status=status.HTTP_400_BAD_REQUEST)
