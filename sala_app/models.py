from django.db import models


class Room(models.Model):
    name_room = models.CharField(max_length=255, unique=True),
    capacity = models.IntegerField(),
    projector_is_available = models.BooleanField()
