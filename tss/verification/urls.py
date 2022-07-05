from django.urls import path
from .views import  *

urlpatterns = [
    path('verify/', verify, name='verify')
]
