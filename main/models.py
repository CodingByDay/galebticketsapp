from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

# GPS OR PAYING DEVICE
class devices(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# PERSON WHO IS GONNA PEFORM

class executives(models.Model):
    executive = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.executive

# TICKET MODEL
class tickets(models.Model):
    location = models.CharField(max_length=200)       
    company = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=200)
    problem = models.CharField(max_length=1000)
    contact_number = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    executive = models.ForeignKey(executives, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.problem

    

    