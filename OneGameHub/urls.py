from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("url_status_checker.urls", namespace="url_status_checker")),
]
