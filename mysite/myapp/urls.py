# django
from django.urls import path

# my_project
from myapp.views import index, contacts, indexItem

urlpatterns = [
    path("hello/", index),  # -> http://127.0.0.1:8000/myapp/hello/
    path(
        "hello/<int:id>/", indexItem, name="detail"
    ),  # -> http://127.0.0.1:8000/myapp/hello/2/
    path("contacts/", contacts),  # -> http://127.0.0.1:8000/myapp/contacts/
]
