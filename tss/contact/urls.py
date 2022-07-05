from django.urls import path
from .views import  *

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('submitquery/', submitquery, name='submitquery'),
    path('subscribe/', subscribe, name='subscribe'),
    path('subscriber-auth/<uidb64>/<token>/',sub_activate, name='activate')
]
