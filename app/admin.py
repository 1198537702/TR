from django.contrib import admin

# Register your models here.
from app.models import Driver, Order, User

admin.site.register(Driver)
admin.site.register(Order)
admin.site.register(User)