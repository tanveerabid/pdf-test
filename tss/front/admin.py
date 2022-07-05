
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from django.contrib.auth.models import User, Group
from .models import *
from country_info_tree.models import *

# Register your models here.


class MyAdminSite(admin.AdminSite):
    site_header = 'TSS Administrator'
    site_title='TSS | SITE ADMIN'
    index_title='HOME'
    enable_nav_sidebar= True

admin_site = MyAdminSite(name='myadmin')





class CountryAdminProvince(ImportExportModelAdmin):
    list_display=['id', 'p_code', 'name','category']
    ordering = ['id']


class CountryAdminDiv(ImportExportModelAdmin):
    list_display=['id', 'province', 'name']
    ordering = ['id']

class CountryAdminDis(ImportExportModelAdmin):
    list_display=['id', 'division', 'name']
    ordering = ['id']

class CountryAdminTeh(ImportExportModelAdmin):
    list_display=['id', 'district', 'name']
    ordering = ['district']

class CountryAdminPhnCode(ImportExportModelAdmin):
    list_display=['id', 'district', 'code']
    ordering = ['id']


        

class AdminQuery(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'subject', 'message', 'date_created', 'date_marked_resolve']





admin_site.register(User)
admin_site.register(Group)

admin_site.register(province, CountryAdminProvince)
admin_site.register(division, CountryAdminDiv)
admin_site.register(district, CountryAdminDis)
admin_site.register(tehsil, CountryAdminTeh)
admin_site.register(phn_code, CountryAdminPhnCode)











