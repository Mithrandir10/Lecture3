from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def isit(request):
    now=datetime.datetime.now()
    return render(request,"hello/index.html",{
        "bday":now.month==10 and now.day==12,"day":now.day,"month":now.month,"yr":now.year
    })
