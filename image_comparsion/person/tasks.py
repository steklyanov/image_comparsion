from celery import shared_task, Celery
from .models import Person

import numpy


@shared_task
def save_vector_to_database(id, array):
    person = Person.objects.get(id=id)
    # vector = array.tolist()
    print(len(array))
    person.vector = array
    person.save()


@shared_task
def euclidean_distance(array1, array2):
    a = numpy.array(array1)
    b = numpy.array(array2)
    dist = numpy.linalg.norm(a-b)
    return dist
