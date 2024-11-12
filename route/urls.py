from django.urls import path
from route import views
from route.views import routes

urlpatterns = [
    path("routes/", views.routes, name="routes"),
    path("routes/<int:id>", views.routeDetail, name="route"),
    path("add-route/", views.addRoute, name="addRoute"),
    path("", routes),
]
