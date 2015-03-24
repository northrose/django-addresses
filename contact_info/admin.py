from django.contrib import admin
from contact_info.models import State, Country, Person, Phone, Email

class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviation']

admin.site.register(State, StateAdmin)
admin.site.register(Country)
admin.site.register(Person)
admin.site.register(Phone)
admin.site.register(Email)