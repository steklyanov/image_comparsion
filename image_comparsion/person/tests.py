from django.test import TestCase
from .models import Person
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status


class PersonTest(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    @staticmethod
    def create_person():
        person = Person.objects.create(
            surname='Surname',
            name='Name'
        )
        return person

    def test_person_created(self):
        """ Test the person string representation """
        person = self.create_person()
        self.assertEqual(str(person), 'Name Surname')

    def test_person_create_api(self):
        """ Test person create api"""
        payload = {'name': 'Name2', 'surname': 'Surname'}
        self.client.post(reverse('person:create'), payload)
        exist = Person.objects.filter(name='Name2').exists()
        self.assertTrue(exist)

    def test_person_list_api(self):
        """ Test person list api """
        person = self.create_person()
        res = self.client.get(reverse('person:list'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['id'], str(person.id))
