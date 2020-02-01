from django.db import models
import uuid
from django.contrib.postgres.fields import ArrayField


class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    vector = ArrayField(models.FloatField(null=True, blank=True), blank=True, null=True)
