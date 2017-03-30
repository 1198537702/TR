from django.contrib import admin

# Register your models here.
from app.models import Driver, Order, User


class DriverAdmin(admin.ModelAdmin):
    list_display = ('tell', 'name', 'licensePlateNumber') # list
    search_fields = ('tell', 'name', 'licensePlateNumber')


class UserAdmin(admin.ModelAdmin):
    list_display = ['tell'] # list
    search_fields = ['tell']


class OrderAdmin(admin.ModelAdmin):
    list_display = ('userId', 'driverId', 'orderTime') # list
    search_fields = ('userId', 'driverId')

admin.site.register(Driver, DriverAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(User, UserAdmin)