from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.mail import send_mail
import datetime 
# Create your models here.
#####################################################################
#####################################################################
#####################################################################
# GPS OR PAYING DEVICE

class devices(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Uredjaj'
        verbose_name_plural = 'Uredjaji'    


# PERSON WHO IS GONNA PEFORM

class executives(models.Model):
    executive = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.executive)

    class Meta:
        verbose_name = 'Serviser'
        verbose_name_plural = 'Serviseri'    


# TICKET MODEL
class tickets(models.Model):
    name = models.ForeignKey(devices, on_delete=models.CASCADE, blank=True, null=True)
    location = models.CharField(max_length=200)       
    company = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=200)
    problem = models.CharField(max_length=1000)
    contact_number = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="authorname", null=True)
    executive = models.ForeignKey(executives, on_delete=models.CASCADE, blank=True, null=True)
    email_as_send = models.BooleanField(default=False)
    SLA = models.DateField()
    
    # Here is the question. They have yearly checkups of devices someone  buys. 
    # They need to be notified 11 months from the last checkup.

    last_checkup = models.DateField()

    def __str__(self):
        return self.problem

    def save(self):
        if self.status == True:
           send_mail("subject", 
           "Zatvoren ticket", 
           "jankojovicic351@gmail.com", 
           [self.author.email], fail_silently=False)
        super().save()


    class Meta:
        verbose_name = 'Tiket'
        verbose_name_plural = 'Tiketi'
# maybeh

    #if tickets.status == True:
     #   pass

    #send mail
#for ticket in tickets:
 #   if tickets.status == True:
        


    
