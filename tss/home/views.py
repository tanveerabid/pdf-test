from django.shortcuts import render

# Create your views here.

# Home view start
def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'home/home.html', context)
# Home view end