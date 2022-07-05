from django.contrib import admin
from front.admin import admin_site
from .models import *

# Register your models here.
class AdminOffice(admin.ModelAdmin):
    list_display = ['office_code', 'province', 'division', 'district', 'tehsil', 
    'post_code',
    'address', 
    'phone_area_code', 
    'phone_num',
    'opening_time', 
    'closing_time',
    'week_start_day', 
    'week_end_day',
    'break_day',
    'friday_break_start',
    'friday_break_end',
    'email',
    'date_created', 
    'date_updated', 'office_status']
    class Media:
        js=("front/js/newajax.js",)


class AdminQuery(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'subject', 'message', 'query_resolve_status', 'date_created', 'date_marked_resolve']

class AdminSubscriber(admin.ModelAdmin):
    list_display = ['id', 'email', 'is_verified', 'sub_status']


admin_site.register(office, AdminOffice)
admin_site.register(query, AdminQuery)
admin_site.register(subscriber, AdminSubscriber)