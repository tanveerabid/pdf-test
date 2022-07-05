from django.shortcuts import render

# Create your views here.

# About view start
def about(request):
    return render(request, 'about/about.html', {'title': 'About Us'})
# About view end