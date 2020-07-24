from django.shortcuts import render
from django import forms
# Create your views here.


class newalph(forms.Form):
    task=forms.CharField(label="New Alphabet")
    prt=forms.IntegerField(label="Priority",max_value=10)
def li(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    if request.method=="POST":
        form=newalph(request.POST)
        if form.is_valid():
            task= form.cleaned_data["task"]
            request.session["tasks"] += [task]
    return render(request,"tasks/index.html",{
        "letters":request.session["tasks"],"form":newalph(),
    })