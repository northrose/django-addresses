from django.contrib import admin
from addresses.models import State

class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviation']

admin.site.register(State, StateAdmin)