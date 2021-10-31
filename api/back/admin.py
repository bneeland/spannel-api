from django.contrib import admin

from . import models

class CourierAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'first_name', 'last_name', 'email', 'city', 'created_at')

class VendorAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'first_name', 'last_name', 'email', 'business_name', 'city', 'created_at')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'first_name', 'last_name', 'email', 'city', 'created_at')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'item_type', 'pickup_date', 'pickup_time', 'dropoff_date', 'dropoff_time', 'courier', 'vendor', 'created_at', 'completed_at')

admin.site.register(models.Courier, CourierAdmin)
admin.site.register(models.Vendor, VendorAdmin)
admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Order, OrderAdmin)
