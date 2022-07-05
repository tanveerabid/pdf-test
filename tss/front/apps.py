from django.contrib.admin.apps import AdminConfig
from django.apps import AppConfig

class MyAdminConfig(AdminConfig):
    default_site = 'front.admin.MyAdminSite'



class FrontConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'front'


