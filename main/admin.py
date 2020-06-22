from django.contrib import admin

# Register your models here.

from .models import devices, executives, tickets

admin.site.register(devices)


admin.site.register(executives)


admin.site.register(tickets)
