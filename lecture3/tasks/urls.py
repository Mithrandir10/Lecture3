from django.urls import path
from . import views

urlpatterns=[
    path("",views.li,name="greek")
]