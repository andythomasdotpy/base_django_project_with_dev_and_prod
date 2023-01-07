from decouple import config

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    print(config("my_project"))
    return HttpResponse("Hello, Hi...Sammie GGGG!!!")