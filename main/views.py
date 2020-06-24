from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import executives, devices, tickets, User
from .forms import CreateNewTicket
# Create your views here.

def index(response, id):
    ls = tickets.objects.get(id=id)
    return render(response, "main/list.html", {"ls":ls})


def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewTicket(response.POST)

        if form.is_valid():            
            location = form.cleaned_data["location"]
            serial_number = form.cleaned_data["serial_number"]
            problem = form.cleaned_data["problem"]
            t = tickets(location=location, serial_number=serial_number, problem=problem)
            t.save()
         
        # push to database.
          
# RANDOM USEFULL COMMENT            
    else:
        form = CreateNewTicket()
    return render(response, "main/create.html", {"form":form})


