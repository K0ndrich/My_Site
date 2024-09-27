# django
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # вход в дамин панель
    path("admin/", admin.site.urls),
    path("myapp/", include("myapp.urls" ,namespace="myapp"))
]
