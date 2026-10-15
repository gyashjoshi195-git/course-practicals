from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    return HttpResponse("Hello, World! - Django")


def home(request):
    return render(request, "hello/home.html", {"name": "Django"})
