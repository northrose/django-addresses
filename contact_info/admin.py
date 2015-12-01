from django.contrib import admin
from django.core import urlresolvers
from contact_info.models import Address, State, Country, Person, Phone, Email


class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviation']


class PersonAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'link_to_address']

    def link_to_address(self, instance):
        self.is_not_used()
        if instance.address:
            url = urlresolvers.reverse("admin:contact_info_address_change", args=[instance.address.id])
            return u'<a href="%s">%s</a>' % (url, instance.address)
        else:
            url = urlresolvers.reverse("admin:contact_info_address_add")
            return u'<a href="%s">add</a>' % (url)
    link_to_address.allow_tags = True
    link_to_address.short_description = "Address"

    def is_not_used(self):
        pass

admin.site.register(Address)
admin.site.register(State, StateAdmin)
admin.site.register(Country)
admin.site.register(Person, PersonAdmin)
admin.site.register(Phone)
admin.site.register(Email)
