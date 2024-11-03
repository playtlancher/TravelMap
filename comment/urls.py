from django.urls import path
from comment import views

urlpatterns = [
    path("routes/<int:id>/comment", views.addComment, name="addComment"),
]
