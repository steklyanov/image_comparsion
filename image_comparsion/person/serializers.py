from .models import Person
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    """ Main serializer for person model"""
    class Meta:
        model = Person
        fields = ['name', 'surname', 'vector']


class PersonRegistrationSerializer(serializers.ModelSerializer):
    """ Serializer for user registration endpoint (without vector)"""

    class Meta:
        model = Person
        fields = ['name', 'surname']
