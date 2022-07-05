from django.urls import path
from .views import  *

urlpatterns = [
    path('download/', download, name='download'),
    path('pdf/', render_pdf_view, name='pdf'),
]