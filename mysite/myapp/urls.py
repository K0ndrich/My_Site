# django
from django.urls import path

# my_project
from myapp.views import index, indexItem

app_name = "myapp"

urlpatterns = [
    path("", index),  # -> http://127.0.0.1:8000/myapp/
    path("<int:my_id>/", indexItem, name="detail"),  # -> http://127.0.0.1:8000/myapp/2/
]


