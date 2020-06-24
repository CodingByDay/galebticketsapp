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
            name = form.cleaned_data["name"]           
            location = form.cleaned_data["location"]
            company = form.cleaned_data["company"]
            serial_number = form.cleaned_data["serial_number"]
            problem = form.cleaned_data["problem"]
            contact_number = form.cleaned_data["contact_number"]
            t = tickets(name=name, location=location, company=company, serial_number=serial_number, problem=problem, contact_number=contact_number)
            t.save()
            response.user.authorname.add(t)
            return HttpResponse("<h1>Uspesno ste prijavili problem. Stice vam mail kada problem bude resen. Hvala. </h1>")
        # push to database.
          # mailing. Add a 
# RANDOM USEFULL COMMENT            
    else:
        form = CreateNewTicket()
    return render(response, "main/create.html", {"form":form})


