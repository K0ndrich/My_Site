# django
from django.shortcuts import render
from django.http import HttpResponse

# my_project
from myapp.models import Product


def index(request):
    items = Product.objects.all()
    context = {"items": items}
    return render(request=request, template_name="myapp/index.html", context=context)


def contacts(request):
    return render(request=request, template_name="myapp/contacts.html")
