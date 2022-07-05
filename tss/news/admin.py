from django.contrib import admin
from front.admin import admin_site
from .models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image', 'category_status']
    list_filter = ['category_status']

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'news_category' , 'keywords', 'description', 'slug', 'content', 'pub_status']
    list_filter = ['news_category', 'pub_status']
    prepopulated_fields = {'slug': ('title',)}


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image_title', 'news', 'image']
    list_filter = ['news']




# asasasa
admin_site.register(News_Category, CategoryAdmin)
admin_site.register(News, NewsAdmin)
admin_site.register(News_Image, ImagesAdmin)