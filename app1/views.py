from django.shortcuts import render

# Create your views here.
"""
My first django view
"""

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('Hello, World!')


def home1(request):
    return HttpResponse('Hello, This is Django based application created')


def welcome(request):
    return render(request, "app1/welcome.html")    # path from templates folder


def another(request):
    return render(request, "app1/dynamic.html", {"name": "Pranit"})