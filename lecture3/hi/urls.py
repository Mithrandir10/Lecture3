from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name="index"),
    path("parteek",views.parteek,name="myname"),
    path("<int:num1>",views.square,name="sq"),
    path("fcb",views.fcb,name="club"),
    
]