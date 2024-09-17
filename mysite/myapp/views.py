from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    items = ["iphone", "xiomi", "samsung"]
    return HttpResponse(items)


def contacts(request):
    return HttpResponse("<h1>Ето Наши Контакты</h1>")
