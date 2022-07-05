"""tss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from front.admin import admin_site
from django.urls import path, include
from country_info_tree.api import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('myadmin/', admin_site.urls),
    path('', include('home.urls')),
    path('', include('services.urls')),
    path('', include('team.urls')),
    path('', include('about.urls')),
    path('', include('contact.urls')),
    path('', include('news.urls')),
    path('', include('verification.urls')),
    path('', include('download.urls')),
    path('divisions/',  DivisionListAPIView.as_view()),
    path('districts/', DistrictListAPIView.as_view()),
    path('tehsils/', TehsilListAPIView.as_view()),
    path('codes/', PhoneCodeListAPIView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)