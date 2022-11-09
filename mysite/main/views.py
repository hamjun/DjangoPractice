from django.shortcuts import render
from django.http import HttpResponse

from .models import ToDoList, Item

# Create your views here.
# Http requests

def index(response, id):
    #html code goes here with http request
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {})
