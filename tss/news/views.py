from django.shortcuts import render
from .models import *
# Create your views here.

# News view start
def news(request):
    return render(request, 'news/news.html', {'title': 'Updates from Us'})
# News view end