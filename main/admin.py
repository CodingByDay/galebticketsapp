from django.contrib.admin import site
from django.contrib import admin
import adminactions.actions as actions
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import devices, executives, tickets

admin.site.register(devices)


admin.site.register(executives) 


class TicketsAdmin(UserAdmin):
    list_display = ('location', 'serial_number', 'status', 'executive', 'SLA', 'last_checkup')
    search_fields = ["location", "serial_number", "status"]
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()

    fieldsets = ()   
    
    ordering = ('status', 'location')

admin.site.register(tickets, TicketsAdmin)

# register all adminactions
actions.add_to_site(site)