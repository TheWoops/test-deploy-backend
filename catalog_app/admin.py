from django.contrib import admin

# Register your models here.
from .models import Customer, System

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'address')
    list_filter = ('name', )

@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display = ('customer', 'host', 'port', 'suffix')
    list_filter = ('customer__name', )


