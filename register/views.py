from django.shortcuts import render, redirect
from .forms import RegisterForm
# Create your views here.
# import massage for succesfull registration
from django.contrib import messages







def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(response, 'Profil uspešno napravljen: ' + user)
        return redirect('login/')    
    else:        
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})
