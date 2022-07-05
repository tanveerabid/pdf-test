from django.contrib import admin
from front.admin import admin_site
from .models import *
# Register your models here.


class AdminDocumentCategory(admin.ModelAdmin):
    list_display = ['name', 'date_added']
    list_filter = ['date_added']

class AdminDocument(admin.ModelAdmin):
    list_display = ['name', 'discription', 'document_category', 'file', 'public_status', 'date_added']
    list_filter = ['document_category']

class AdminInvoice(admin.ModelAdmin):
    list_display = ['name', 'business', 'ntn', 'date_added']
    list_filter = ['ntn']

admin_site.register(document_category, AdminDocumentCategory)
admin_site.register(document, AdminDocument)
admin_site.register(invoice, AdminInvoice)