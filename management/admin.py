from django.contrib import admin
from .models import Factory, Car, Dealership, Client

admin.site.site_header = "Automotive Admin"
admin.site.site_title = "Automotive Admin Area"
admin.site.index_title = "Welcome to the Automotive Admin Area"

admin.site.register(Factory)
admin.site.register(Car)
admin.site.register(Dealership)
admin.site.register(Client)


# class CarInLine(admin.TabularInline):
#     model = Car
#     extra = 1
#
#
# class FactoryAdmin(admin.ModelAdmin):
#     fieldsets = [(None, {'fields': ['name', 'address']}), ]
#     inlines = [CarInLine]


#admin.site.register(Factory, FactoryAdmin)
