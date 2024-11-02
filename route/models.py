from django.db import models

from tag.models import Tag


class Route(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    short_description = models.TextField()
    description = models.TextField()
    start = models.JSONField(blank=True, null=True)
    end = models.JSONField(blank=True, null=True)
    def __str__(self):
        return self.name

class Waypoint(models.Model):
    route = models.ForeignKey('Route', on_delete=models.CASCADE, related_name='waypoints')
    location = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.location
