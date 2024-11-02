from django.urls import path
from route import views
from route.views import mainPage

urlpatterns = [
    path("main-page/", views.mainPage, name="mainPage"),
    path("routes/<int:id>", views.routeDetail, name="route"),
    path("add-route/", views.addRoute, name="addRoute"),
    path("", mainPage),
]
