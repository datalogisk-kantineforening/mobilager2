from django.contrib import admin

from .models import Vendor, Product, EventType

class VendorAdmin(admin.ModelAdmin):
    fields = ['name']

class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'vendor', 'quantity', 'category', 'discontinued']

admin.site.register(Vendor, VendorAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(EventType)
