from django.http import HttpResponse
from django.shortcuts import render

def world(request):
    return HttpResponse("Hello, world!")

def hello(request, name):
    return render(request, "hello/hello.html", {
        "name": name.capitalize()
    })
