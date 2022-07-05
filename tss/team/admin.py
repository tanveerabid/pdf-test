from django.contrib import admin
from front.admin import admin_site
from .models import *
# Register your models here.

class AdminEmployee(admin.ModelAdmin):
    list_display = ['office', 'name', 'designation', 'cnic', 'date_added']

class AdminEmployeeProfile(admin.ModelAdmin):
    list_display = ['cnic', 'address', 'img', 'cell_number', 'fb', 'twitt', 'linkedin', 'insta', 'date_added']

admin_site.register(employee, AdminEmployee)
admin_site.register(employee_profile, AdminEmployeeProfile)