from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello")

def parteek(request):
    return HttpResponse(", Parteek")

def square(request, num1):
    return render(request, "hello/sq.html", {
        "num": num1,"res": num1*num1
    }) 

def fcb(request):
    return render(request, "hello/fcb.html")