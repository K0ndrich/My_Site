# django
from django.urls import path

# my_project
from myapp.views import index, indexItem, add_item , update_item

app_name = "myapp"

urlpatterns = [
    path("", index , name="index"),  # -> http://127.0.0.1:8000/myapp/
    path("<int:my_id>/", indexItem, name="detail"),  # -> http://127.0.0.1:8000/myapp/2/
    path(
        "add_item/", add_item, name="detail"
    ),  # ->http://127.0.0.1:8000/myapp/add_item/
    path("update_item/<int:my_id>/", update_item, name="update_item"),
]
