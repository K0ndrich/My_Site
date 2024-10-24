# django
from django.shortcuts import render
from django.http import HttpResponse

# my_project
from myapp.models import Product


# главная страница сайта со всеми главынми товарами
def index(request):
    items = Product.objects.all()
    context = {"items": items}
    return render(request=request, template_name="myapp/index.html", context=context)


# страница для обозначений одной записи товара на сайте
# id значение передаеться пользователем в url-адрессе  # -> http://127.0.0.1:8000/myapp/hello/id/
def indexItem(request, my_id):
    item = Product.objects.get(id=my_id)
    context = {"item": item}
    return render(request=request, template_name="myapp/detail.html", context=context)


# страница для добавление нового товара на сайт
def add_item(request):
    return render(request, template_name="myapp/additem.html")
