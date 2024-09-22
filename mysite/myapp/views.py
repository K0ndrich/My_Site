# django
from django.shortcuts import render
from django.http import HttpResponse

# my_project
from myapp.models import Product


def index(request):
    items = Product.objects.all()
    return HttpResponse(items)


def contacts(request):
    return HttpResponse("<h1>Ето Наши Контакты</h1>")
