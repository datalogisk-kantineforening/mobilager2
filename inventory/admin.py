from django.contrib import admin

from .models import Vendor, User, Product, EventType

class VendorAdmin(admin.ModelAdmin):
    fields = ['name']

class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'vendor', 'quantity', 'discontinued']

admin.site.register(Vendor, VendorAdmin)
admin.site.register(User)
admin.site.register(Product, ProductAdmin)
admin.site.register(EventType)
