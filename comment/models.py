from django.contrib.auth.models import User
from django.db import models
from route.models import Route


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    content = models.TextField()
