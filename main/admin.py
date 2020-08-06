from django.contrib.admin import site
from django.contrib import admin
import adminactions.actions as actions

# Register your models here.

from .models import devices, executives, tickets

admin.site.register(devices)


admin.site.register(executives)


admin.site.register(tickets)


# register all adminactions
actions.add_to_site(site)