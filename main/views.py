from django.shortcuts import render
from django.http import HttpResponse
from .models import executives, devices, tickets
from .forms import CreateNewTicket
# Create your views here.

def index(response):
    return render(response, "main/base.html", {})


def home(response):
    return render(response, "main/home.html", {})

def create(response):
    # Defining a simple form for the data.
    form = CreateNewTicket()
    return render(response, "main/create.html", {"form":form})


