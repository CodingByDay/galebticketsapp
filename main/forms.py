from django import forms
from .models import tickets, devices, executives





class CreateNewTicket(forms.Form):

    # Add a dropdown menu for "GPS" or "Fiskalni program"
    name = forms.ModelChoiceField(queryset=devices.objects.all())
    location = forms.CharField(label="Location:", max_length=200)
    company = forms.CharField(label="Company:", max_length=200)
    serial_number = forms.CharField(label="Serial Number:", max_length=200)
    problem = forms.CharField(label="Describe a problem:", max_length=200)
    contact_number = forms.CharField(label="Your number:", max_length=20)

   