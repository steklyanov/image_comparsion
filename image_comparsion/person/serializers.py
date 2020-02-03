from .models import Person, Image
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    """ Main serializer for person model"""
    class Meta:
        model = Person
        fields = ['name', 'surname', 'vector']


class ListIdSerializer(serializers.ModelSerializer):
    """ Serializer for displaying only User ID's"""
    class Meta:
        model = Person
        fields = ['id']


class ImageSerializer(serializers.ModelSerializer):
    """ Serializer for image uploading"""
    class Meta:
        model = Image
        fields = ['image']
