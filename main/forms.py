from django import forms


class CreateNewTicket(forms.Form):
    # Add a dropdown menu for "GPS" or "Fiskalni program"
    location = forms.CharField(label="Location:", max_length=200)
    company = forms.CharField(label="Company:", max_length=200)
    serialNumber = forms.CharField(label="Serial Number:", max_length=200)
    problem = forms.CharField(label="Describe a problem:", max_length=200)
    contactNumber = forms.CharField(label="Your number:", max_length=20)

