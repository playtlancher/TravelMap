from django.urls import path
from user import views

urlpatterns = [
    path("login/", views.loginHandler, name="login"),
    path("registration/", views.registrationHandler, name="registration"),

]
