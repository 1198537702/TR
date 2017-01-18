from django.contrib import admin

# Register your models here.
from .models import TestTable
admin.site.register(TestTable)