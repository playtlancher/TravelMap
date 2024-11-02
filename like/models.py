from django.contrib.auth.models import User
from django.db import models

from route.models import Route


# Create your models here.
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    route = models.ForeignKey(Route , on_delete=models.CASCADE)