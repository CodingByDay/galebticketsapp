from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import executives, devices, tickets, User
from .forms import CreateNewTicket
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from django.core.mail import send_mail





def home(response):
    return render(response, "main/home.html", {})

 

# Restrict acces to unauthorized users
@login_required(login_url="../login/")
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
            messages.success(response, "Uspesno ste prijavili tiket. Na vas email ce stici obavestenje.")

            # send an emmail
            send_mail(
               'Otvoren tiket', # Mail title
                problem, # massage
               'jankojovicic351@gmail.com', # From
               ['jankojovicicwork@gmail.com'] # To email
                )
          
# RANDOM USEFULL COMMENT            
    else:
        form = CreateNewTicket()
    return render(response, "main/create.html", {"form":form})


def logoutUser(response):
    logout(response)
    return redirect('../login/')
