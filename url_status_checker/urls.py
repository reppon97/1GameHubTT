from django.urls import path

from url_status_checker import views

app_name = "url_status_checker"

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.index, name="index"),
    path("register/", views.register, name="register"),
]
