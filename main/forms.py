from django import forms
from .models import tickets, devices, executives





class CreateNewTicket(forms.Form):

    # Add a dropdown menu for "GPS" or "Fiskalni program"
    name = forms.ModelChoiceField(queryset=devices.objects.all())
    location = forms.CharField(label="Lokacija:", max_length=200)
    company = forms.CharField(label="Kompanija:", max_length=200)
    serial_number = forms.CharField(label="Serijski broj:", max_length=200)
    problem = forms.CharField(label="Opišite problem:", max_length=200)
    contact_number = forms.CharField(label="Vaš broj telefona:", max_length=20)

   